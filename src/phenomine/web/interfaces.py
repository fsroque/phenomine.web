from zope.interface import Interface, implements
from zope import schema

import suds.client

from phenomine.web import config

class ISearch(Interface):
    """Main search form"""
    
    phenotypes = schema.Text(
        title = u'List of phenotypes for searching.',
        description = u"""
        A list of phenotypes to be used when searching the OMIM database,
        one line per search term. Exact match only.
        """,
        required = False
    )
    
    search = schema.Choice(
        title = u'Use text-mining?',
        description = u"""
        Should the search use text-mining? If 'no', then only morbidmap associations will be used. If 'partial', in addition to morbidmap genes, the OMIM phenotype descriptions for which the molecular basis is known will be mined for occurrences of the phenotype. If 'full', all of the phenotypes will be included in the text mining search, including those for which the molecular basis is unknown.
        """,
        values = [u"no",u"partial",u"full"],
        default = u"no",
        required = True
    )
        
class IPhenomineWebService(Interface):
    """Class to interface the phenomine Web Service"""
    pass
    

class PhenomineWebService(object):
    implements(IPhenomineWebService)

    def __init__(self):
        # import pdb;pdb.set_trace()
        self.client = suds.client.Client(config.wsdl, cache=None)
        
    def _runService(self,phenotype_list,search_option):
        return self.client.service.Run(phenotype_list,search_option)
    
    def getVersion(self):
        return self.client.service.Version()
        
    def getGeneList(self,phenotypes,search_option):
        # import pdb;pdb.set_trace()
        if search_option == 'no':
           search_option='false' 
        phenotype_list = phenotypes.split('\n')
        web_results = self._runService(phenotype_list,search_option)
        results = []
        if len(web_results.geneList) > 0:
            for item in web_results.geneList.gene:
                res = dict()
                res['phenotype'] = item['phenotype']
                res['matched_morbid'] = item['matched_morbid']
                res['ensembl'] = item['ensembl']
                res['hgnc'] = item['hgnc']
                res['mim'] = item['mim']
                if search_option != 'false' and item['matched_snippet'] is not None:
                    res['match'] = item['matched_snippet']
                else:
                    res['match'] = ''
                results.append(res)
        return (results, web_results.report)