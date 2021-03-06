from setuptools import setup, find_packages

version = '1.0'

setup(name='phenomine.web',
      version=version,
      description="",
      long_description="""\
""",
      # Get strings from http://pypi.python.org/pypi?:action=list_classifiers
      classifiers=[],
      keywords="",
      author="",
      author_email="",
      url="",
      license="",
      package_dir={'': 'src'},
      packages=find_packages('src'),
      namespace_packages=['phenomine',],
      include_package_data=True,
      zip_safe=False,
      install_requires=['setuptools',
                        'grok',
                        'grokui.admin',
                        'fanstatic',
                        'zope.fanstatic',
                        'grokcore.startup',
                        # Add extra requirements here
                        'suds',
                        'js.jquery',
                        ],
      entry_points={
          'fanstatic.libraries': [
              'phenomine.web = phenomine.web.resource:library',
          ]
      })
