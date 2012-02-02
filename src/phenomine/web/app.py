import grok
import zope.interface
from zope.session.interfaces import ISession
from zope.app.publication.interfaces import IBeforeTraverseEvent

import re
import time

from phenomine.web import resource
from phenomine.web.interfaces import ISearch, PhenomineWebService

from js.jquery import jquery
from js.jquery_tablesorter import tablesorter



class Phenomine(grok.Application, grok.Container):
    pass

@grok.subscribe(Phenomine, IBeforeTraverseEvent)
def handle(obj, event):
    resource.framework.need()
    resource.favicon.need()
    resource.style.need()
    jquery.need()
    tablesorter.need()
    resource.javascript.need()
    resource.framework_js.need()
    resource.elastic_textarea.need()

class Phenominemacro(grok.View):
    # Macropage
    grok.context(zope.interface.Interface)

class Index(grok.View):
    grok.context(Phenomine)
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
    grok.context(Phenomine)
    """Front page search form"""
    template = grok.PageTemplateFile('forms/search.pt')
    form_fields = grok.AutoFields(ISearch)
    searchPhenomine = PhenomineWebService()
    
    @property
    def filters(self):
      return ISession(self.request)['filters']
              
    @property
    def result(self):
        return ISession(self.request)['result']
        
    def doSearch(self):
        (self.result['phenomine'],self.result['report']) = self.searchPhenomine.getGeneList(self.filters['phenotypes'], self.filters['search'])
        

    @grok.action('Clear', validator=None, name="clearHome")
    def clear(self, **data):
        if self.filters.has_key('phenotypes'):
            del(self.filters['phenotypes'])
        if self.filters.has_key('search'):
            del(self.filters['search'])
        if self.result.has_key('phenomine'):
            del(self.result['phenomine'])
        
    @grok.action('Search', validator=validateForm, name="searchHome")
    def search(self, **data):
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
        if self.result.has_key('phenomine'):
            return True
        return False
    
    def getResult(self):
        if self.hasResult:
            return self.result['phenomine']
        return ''
    
    def getReport(self):
        if self.hasResult:
            return self.result['report']
        return ''
    
    def getLastUpdate(self):
        # searchPhenomine = PhenomineWebService()
        last_update = self.searchPhenomine.getVersion()
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