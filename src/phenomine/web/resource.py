from fanstatic import Library, Resource

library = Library('phenomine.web', 'static')

style = Resource(library, 'css/phenomine.css')
javascript = Resource(library, 'js/phenomine.js')
tablesorter = Resource(library, 'css/tablesorter.css')
framework = Resource(library, 'bootstrap/css/bootstrap.css', minified='bootstrap/css/bootstrap.min.css')
framework_js = Resource(library, 'bootstrap/js/bootstrap.js', minified='bootstrap/js/bootstrap.min.js')
favicon = Resource(library, 'favicon.ico')
elastic_textarea = Resource(library, 'js/jquery.elastic.js')