import os
import logging
import ConfigParser

# Root directory
filepath = os.path.abspath(__file__)
basepath = os.path.dirname(filepath)
srcpath = os.path.split(basepath)[0]
ROOT_DIR = os.path.split(srcpath)[0]

# Read config file
config = ConfigParser.ConfigParser()
config.readfp(open(os.path.join('parts', 'etc', 'omimine.web.ini')))

# WSDL location
wsdl = config.get('omimine', 'WSDL')