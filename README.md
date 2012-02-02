# phenomine.web - A web interface for the phenomine Web Service using grok

## Latest updates
* [2012-02-01] - Initial import

## About

First public release of phenomine.web, a web frontent built in a grok installation to query the [phenomine][phenomine] Web Service.

## Features
* 100% pure Python, built atop the excelent [Grok Zope framework][grok]
* Self hosted, or distributable to any existing grok installation
* Templates use the [bootstrap][bs] framework 

## Roadmap
* Add better error handling
* Introduce logging

## Requirements
* Python 2.6 (2.7 will work just as well)
* Access to the phenomine Web Service

## Running phenomine.web
* Modify the file etc/phenomine.web.ini.in to point to the appropriate location of the phenomine Web Service [WSDL][wsdl]
* Run python bootstrap.py to create the buildout executable
* Run ./bin/buildout to download necessary packages and create the appropriate folder structure
* Run ./bin/paster serve /parts/etc/deploy.ini
* That's it!

## License

phenomine.web is released under the [MIT License][mit]. 

[mit]: http://www.opensource.org/licenses/mit-license.php
[phenomine]:https://github.com/fsroque/phenomine
[grok]:http://grok.zope.org/
[bs]:http://twitter.github.com/bootstrap/
[wsdl]:http://www.w3.org/TR/wsdl