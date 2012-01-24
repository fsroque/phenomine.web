import grok
import zope.interface
from zope.session.interfaces import ISession
from zope.app.publication.interfaces import IBeforeTraverseEvent

import re
import time

from omimine.web import resource
from omimine.web.interfaces import ISearch, OmimineWebService

from js.jquery import jquery
from js.jquery_tablesorter import tablesorter



class Omimine(grok.Application, grok.Container):
    pass

@grok.subscribe(Omimine, IBeforeTraverseEvent)
def handle(obj, event):
    resource.blueprint_screen.need()
    resource.favicon.need()
    resource.style.need()
    jquery.need()
    tablesorter.need()
    resource.javascript.need()
    resource.tablesorter.need()
    # add fixes for IE in css
    if event.request.get('HTTP_USER_AGENT').find('MSIE') > -1:
        resource.blueprint_ie.need()

class Omiminemacro(grok.View):
    # Macropage
    grok.context(zope.interface.Interface)

class Index(grok.View):
    grok.context(Omimine)
    grok.name('index')
    def update(self):
        pass
    
    def searchForm(self):
        form = SearchForm(self.context, self.request)
        phenotypes = self.request.get("form.phenotypes")
        search = self.request.get('form.search')
        if (phenotypes is not None and phenotypes != ''):
            form.filters['phenotypes'] = phenotypes
            form.filters['search'] = search
            # form.doSearch()
        
        return form()

def validateForm(form, action, data):
    form.validate(action, data)
    
    err_msg = []
    if not data.has_key('phenotypes'):
        err_msg.append('<strong>Input error:</strong> You must specify a list of phenotypes')
    elif data['phenotypes'] is None or data['phenotypes'] == '':
        err_msg.append('<strong>Input error:</strong> You must specify a list of phenotypes')
        
    return err_msg

class SearchForm(grok.Form):
    grok.context(Omimine)
    """Front page search form"""
    template = grok.PageTemplateFile('forms/search.pt')
    form_fields = grok.AutoFields(ISearch)
    searchOmimine = OmimineWebService()
    
    @property
    def filters(self):
      return ISession(self.request)['filters']
              
    @property
    def result(self):
        return ISession(self.request)['result']
        
    def doSearch(self):
        (self.result['omimine'],self.result['report']) = self.searchOmimine.getGeneList(self.filters['phenotypes'], self.filters['search'])
        

    @grok.action('Clear', validator=None, name="clearHome")
    def clear(self, **data):
        if self.filters.has_key('phenotypes'):
            del(self.filters['phenotypes'])
        if self.filters.has_key('search'):
            del(self.filters['search'])
        if self.result.has_key('omimine'):
            del(self.result['omimine'])
        
    @grok.action('Search OMIM', validator=validateForm, name="searchHome")
    def searchOMIM(self, **data):
        phenotypes = data['phenotypes']
        search = data['search']
        self.filters['phenotypes'] = phenotypes
        self.filters['search'] = search
        self.doSearch()
    
    def getPhenotypeInput(self):
        if self.filters.has_key('phenotypes'):
            return self.filters['phenotypes']
        return ''
    
    def getSearchInput(self):
        if self.filters.has_key('search'):
            return self.filters['search']
        return ''
    
    def hasResult(self):
        if self.result.has_key('omimine'):
            return True
        return False
    
    def getResult(self):
        if self.hasResult:
            return self.result['omimine']
        return ''
    
    def getReport(self):
        if self.hasResult:
            return self.result['report']
        return ''
    
    def getLastUpdate(self):
        # searchOmimine = OmimineWebService()
        last_update = self.searchOmimine.getVersion()
        m = re.search('OMIM updated: (\d\d\d\d-\d\d-\d\d)', last_update)
        return time.strftime('%d %B %Y',time.strptime(m.group(1),'%Y-%m-%d'))
        
    def returnMorbid(self, morbid):
        """returns the morbid info, hyperlinking the entry if applicable"""
        m = re.search(', (\d+) \(',morbid)
        if m:
            return re.sub(m.group(1),'<a href="http://www.omim.org/entry/%s" target="_blank">%s</a>' % (m.group(1),m.group(1)),morbid)
        else:
            return morbid
    
    def tableHeader(self):
        header = '<em>Found <strong>%d</strong> matches.</em>' % len(self.getResult())
        header = header + '<a href="%s">Download report</a>' % self.getReport()
        return header