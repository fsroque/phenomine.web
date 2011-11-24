import grok
import zope.interface
from zope.session.interfaces import ISession

import suds.client

from omimine.web import resource
from omimine.web.interfaces import ISearch
from omimine.web import config

class Omimine(grok.Application, grok.Container):
    pass


class Omiminemacro(grok.View):
    # Macropage
    grok.context(zope.interface.Interface)

class Index(grok.View):
    grok.context(Omimine)
    grok.name('index')
    def update(self):
        resource.style.need()
    
    @property
    def filters(self):
        return ISession(self.request)['filters']
    
    @property
    def result(self):
        return ISession(self.request)['result']
    
    def searchForm(self):
        form = SearchForm(self.context, self.request)
        phenotypes = self.request.get("form.phenotypes")
        if phenotypes is not None and phenotypes != '':
            form.filters['phenotypes'] = phenotypes
            form.doSearch()
        
        return form()

def validateForm(form, action, data):
    form.validate(action, data)
    
    err_msg = []
    if not data.has_key('phenotypes'):
        err_msg.append('phenotypes filter not provided')
    elif  data['phenotypes'] is None or data['phenotypes'] == '':
        err_msg.append('phenotypes filter not provided')
        
    return err_msg

class SearchForm(grok.Form):
    grok.context(Omimine)
    """Front page search form"""
    template = grok.PageTemplateFile('forms/search.pt')
    form_fields = grok.AutoFields(ISearch)
    
    @property
    def filters(self):
        return ISession(self.request)['filters']
    
    @property
    def result(self):
        return ISession(self.request)['result']
        
    def doSearch(self):
        self.result['omimine'] = self.filters['phenotypes']

    @grok.action('Clear', validator=None, name="clearHome")
    def clear(self, **data):
        if self.filters.has_key('phenotypes'):
            del(self.filters['phenotypes'])
        if self.result.has_key('omimine'):
            del(self.result['omimine'])
        
    @grok.action('Search OMIM', validator=validateForm, name="searchHome")
    def searchOMIM(self, **data):
        phenotypes = data['phenotypes'] 
        self.filters['phenotypes'] = phenotypes
        self.doSearch()
        # search = Search()
        # self.applyData(search,**data)
        # 
        # import datetime
        # name = str(datetime.datetime.now()).replace(' ','-')
        # 
        # name = str('phenotypes')
        #         
        # self.context[name] = search
        # 
        # return self.redirect(self.url(self.context[name]))
        # import pdb; pdb.set_trace()
        # client = suds.client.Client(config.wsdl, cache=None)
        # 
        # phenotypes = data['phenotypes'].split('\n')
        # search = data['search']
        # 
        # if search == 'no':
        #     search = 'false'
        # 
        # results = client.service.Run(phenotypes,search)
        
        pass
    
    def getPhenotypeInput(self):
        if self.filters.has_key('phenotypes'):
            return self.filters['phenotypes']
        else:
            return ''
    
    def getSearchInput(self):
        return self.sessionData['search']
    
# class SearchView(grok.View):
#     """Displays search results"""
#     grok.context(Search)
#     grok.name('index')
#     
#     def render(self):
#         return """
#         <html><body>
#         <p>phenotypes: %s</p>
#         <p>search: %s</p>
#         </body></html>
#         """ % (self.context.phenotypes,self.context.search)
        
        
