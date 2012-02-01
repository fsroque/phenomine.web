from fanstatic import Library, Resource

library = Library('phenomine.web', 'static')

style = Resource(library, 'phenomine.css')
javascript = Resource(library, 'phenomine.js')
tablesorter = Resource(library, 'tablesorter.css')
framework = Resource(library, 'bootstrap/css/bootstrap.css', minified='bootstrap/css/bootstrap.min.css')
framework_js = Resource(library, 'bootstrap/js/bootstrap.js', minified='bootstrap/js/bootstrap.min.js')
favicon = Resource(library, 'favicon.ico')