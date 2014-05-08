#!/usr/bin/env python
import os

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

with open(os.path.join(os.path.dirname(__file__), 'README.rst')) as readme:
    long_description = readme.read()


setup(name='pyBreezeChMS',
      version='0.1.0',
      description="Python interface to BreezeChMS REST API.",
      long_description=long_description,
      classifiers=[
          'Development Status :: 1 - Planning',
          'Environment :: Console',
          'Intended Audience :: Developers',
          'License :: OSI Approved :: MIT License',
          'Operating System :: OS Independent',
          'Programming Language :: Python :: 2.6',
          'Programming Language :: Python :: 2.7',
          'Natural Language :: English',
      ],
      keywords='breezechms breezeapi python',
      author='Alex Ortiz',
      author_email='aortiz32@gmail.com',
      maintainer='Alex Ortiz',
      maintainer_email='aortiz32@gmail.com',
      url='http://ozgur.github.com/pyBreezeChMS/',
      license='MIT',
      packages=['breeze'],
      test_suite='tests.all_tests',
      zip_safe=False,
)