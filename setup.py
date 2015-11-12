#!/usr/bin/env python
'''
Created on Nov 6, 2011

@author: hugosenari
'''

from distutils.core import setup

with open('README.rst') as readme_file:
    readme = readme_file.read()

setup(name='mpris2',
      version='1.0.1',
      description='Python mpris2 definition',
      author='hugosenari',
      author_email='hugosenari@gmail.com',
      url='https://github.com/hugosenari/mpris2',
      keywords = ["dbus", "mpris2"],
      packages=('mpris2', 'mpris2.decorator', 'mpris2.types'),
      requires=(),
      license = "GPL",
      classifiers=[
            "Development Status :: 3 - Alpha",
            "Intended Audience :: Developers",
            "Topic :: Multimedia :: Sound/Audio",
            "Topic :: Software Development :: Libraries :: Python Modules",
            "License :: OSI Approved :: GNU General Public License (GPL)",
            "Programming Language :: Python :: 2.7",
            "Programming Language :: Python :: 3.4"
      ],
      long_description = readme
)