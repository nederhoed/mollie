from distutils.core import setup
from distutils.command.install_scripts import install_scripts

import os, sys
from glob import fnmatch

import version

ignore = ('CVS', )
        
setup(name = "mollie", 
      version = version.version,
      maintainer = 'Ivo van der Wijk',
      maintainer_email = 'ivo@m3r.nl',
      author = 'Ivo van der Wijk',
      author_email = 'ivo@m3r.nl',
      platforms = ['any'],
      url = 'http://projects.m3r.nl/opensource/trac/mollie',
      description = 'Mollie.nl SMS gateway API',
      long_description = 
"""An API Implementation for the mollie.nl SMS Gateway""",
      license = "BSD License",
      packages = ["mollie"],
)
