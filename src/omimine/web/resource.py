from fanstatic import Library, Resource

library = Library('omimine.web', 'static')

style = Resource(library, 'omimine.css')
javascript = Resource(library, 'omimine.js')
tablesorter = Resource(library, 'tablesorter.css')
blueprint_screen = Resource(library, 'blueprint/screen.css')
blueprint_print = Resource(library, 'blueprint/print.css')
blueprint_ie = Resource(library, 'blueprint/ie.css')
favicon = Resource(library, 'favicon.ico')