import gupass

from setuptools import setup

setup(name='GuPass',
      version=gupass.version,
      author='w3security',
      author_email='alerts@log4j.codes',
      license='MIT',
      description='GuPass is a Guess tool for custom wordlist generation. It utilizes common human paradigms for constructing passwords and can output the full wordlist or rules.',
      keywords='wordlist wordlist-generator passwords',
      packages=['gupass', 'gupass.view', 'gupass.data', 'tests',
                'gupass.icons'],
      entry_points={'gui_scripts': 'gupass = gupass.controller:main'},
      test_suite='tests.test_model',
      setup_requires=['pytest-runner'],
      tests_require=['pytest'],
      package_data={'gupass': ['data/*.txt', 'data/*.psv']},
      include_package_data=True,
      )