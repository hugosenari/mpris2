#!/usr/bin/env python
'''
Created on Nov 6, 2011

@author: hugosenari
'''

from distutils.core import setup

with open('README.rst') as readme_file:
    readme = readme_file.read()

setup(name='mpris2',
      version='0.9',
      description='Python mpris2 definition',
      author='hugosenari',
      author_email='hugosenari@gmail.com',
      url='https://github.com/hugosenari/mpris2',
      keywords = ["dbus", "mpris2"],
      packages=('mpris2',),
      requires=(),
      license = "GPL",
      classifiers=[
            "Development Status :: 4 - Beta",
            "Environment :: X11 Applications",
            "Intended Audience :: Developers",
            "License :: OSI Approved :: GNU General Public License (GPL)",
            "Programming Language :: Python :: 2.7",
            "Topic :: Software Development :: Libraries :: Python Modules",
      ],
      long_description = readme
)