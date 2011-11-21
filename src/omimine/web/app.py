import grok
from zope.session.interfaces import ISession

import suds.client

from omimine.web import resource
from omimine.web.interfaces import ISearch
from omimine.web import config

class Omimine(grok.Application, grok.Container):
    pass


class Index(grok.View):
    grok.context(Omimine)
    grok.name('index')
    def update(self):
        resource.style.need()
    
    @property
    def sessionData(self):
        return ISession(self.request)
    
    def searchForm(self):
        form = SearchForm(self.context, self.request)
        phenotypes = self.request.get("phenotypes")
        search = self.request.get("search")
        
        if phenotypes is not None and phenotypes != '':
            form.sessionData['phenotypes'] = phenotypes
        if search is not None and search != '':
            form.sessionData['search'] = search
        
        if (phenotypes is not None and phenotypes != '') and (search is not None and search != ''):
            form.doSearch()
        
        return form()

def validateForm(form, action, data):
    form.validate(action, data)
    pass

class SearchForm(grok.Form):
    grok.context(Omimine)
    """Front page search form"""
    template = grok.PageTemplateFile('forms/search.pt')
    # form_fields = grok.AutoFields(ISearch)
    
    @property
    def sessionData(self):
        return ISession(self.request)['session']
        
    def doSearch(self):
        """docstring for doSearch"""
        pass
    
    @grok.action('Search OMIM', validator=validateForm, name="searchHome")
    def searchOMIM(self, **data):
        try:
            self.sessionData['phenotypes'] = data['phenotypes']
        except:
            self.sessionData['phenotypes'] = ''
            
        try:
            self.sessionData['search'] = data['search']
        except:
            self.sessionData['search'] = ''
        
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
        return self.sessionData['phenotypes']
    
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
        
        
