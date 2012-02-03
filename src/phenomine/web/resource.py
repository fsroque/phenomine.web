from fanstatic import Library, Resource

library = Library('phenomine.web', 'static')

style = Resource(library, 'css/phenomine.css')
javascript = Resource(library, 'js/phenomine.js')
framework = Resource(library, 'bootstrap/css/bootstrap.css', minified='bootstrap/css/bootstrap.min.css')
framework_js = Resource(library, 'bootstrap/js/bootstrap.js', minified='bootstrap/js/bootstrap.min.js', bottom=True)
favicon = Resource(library, 'favicon.ico')
elastic_textarea = Resource(library, 'js/jquery.elastic.js', minified='js/jquery.elastic.min.js')
datatables_js = Resource(library, 'datatables/js/jquery.dataTables.js', minified='datatables/js/jquery.dataTables.min.js',  bottom=True)
tabletools_js = Resource(library, 'datatables/js/TableTools.js', minified='datatables/js/TableTools.min.js', bottom=True)
tabletools_js_zeroclipboard =  Resource(library, 'datatables/js/ZeroClipboard.js',  bottom=True)
tabletools_css =  Resource(library, 'datatables/css/TableTools.css')