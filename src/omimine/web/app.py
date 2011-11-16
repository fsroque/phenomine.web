import grok

from omimine.web import resource

class Omimine(grok.Application, grok.Container):
    pass

class Index(grok.View):
    def update(self):
        resource.style.need()
