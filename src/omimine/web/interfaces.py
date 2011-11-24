from zope import interface
from zope import schema

class ISearch(interface.Interface):
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
        