from setuptools import setup, find_packages

version = '0.1'

setup(name='omimine.web',
      version=version,
      description="",
      classifiers=[], 
      keywords="",
      author=["Francisco Roque"],
      author_email=["francisco.roque@uni.no"],
      url="",
      license="",
      package_dir={'': 'src'},
      packages=find_packages('src'),
      namespace_packages=['omimine',],
      include_package_data=True,
      zip_safe=False,
      install_requires=['setuptools',
                        'grok',
                        'grokui.admin',
                        'z3c.testsetup',
                        'grokcore.startup',
                        # Add extra requirements here
                        'suds',
                        'megrok.menu',
                        'twill',
                        'mr.developer',
                        ],
      entry_points = """
      [console_scripts]
      web-debug = grokcore.startup:interactive_debug_prompt
      web-ctl = grokcore.startup:zdaemon_controller
      web-test = omimine.web_test.all_tests:main
      [paste.app_factory]
      main = grokcore.startup:application_factory
      """,
      )
