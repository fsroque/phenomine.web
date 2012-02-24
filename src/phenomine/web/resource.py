from fanstatic import Library, Resource

library = Library('phenomine.web', 'static')

style = Resource(library, 'css/phenomine.css')
javascript = Resource(library, 'js/phenomine.js')
framework = Resource(library, 'css/bootstrap.css', minified='css/bootstrap.min.css')
framework_js = Resource(library, 'js/bootstrap.js', minified='js/bootstrap.min.js')
favicon = Resource(library, 'favicon.ico')
elastic_textarea = Resource(library, 'js/jquery.elastic.js', minified='js/jquery.elastic.min.js')
datatables_js = Resource(library, 'js/jquery.dataTables.js', minified='js/jquery.dataTables.min.js')
tabletools_js = Resource(library, 'js/TableTools.js', minified='js/TableTools.min.js', depends=[datatables_js])
tabletools_js_zeroclipboard =  Resource(library, 'js/ZeroClipboard.js',  bottom=True)
tabletools_css =  Resource(library, 'css/TableTools.css')
