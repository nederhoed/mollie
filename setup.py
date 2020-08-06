from setuptools import setup

import version

ignore = ('CVS', )

setup(name = "molliesms",
      version = version.version,
      maintainer = 'Ivo van der Wijk',
      maintainer_email = 'ivo@m3r.nl',
      author = 'Ivo van der Wijk',
      author_email = 'ivo@m3r.nl',
      platforms = ['any'],
      url = 'https://github.com/iivvoo/mollie',
      description = 'Mollie.nl SMS gateway API in Python',
      long_description = """\
A Python API Implementation for the mollie.nl SMS Gateway""",
      license = "BSD License",
      packages = ["molliesms"],
      )
