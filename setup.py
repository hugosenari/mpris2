#!/usr/bin/env python
'''
Created on Nov 6, 2011

@author: hugosenari
'''

from distutils.core import setup

setup(name='mpris2',
      version='0.9',
      description='Python mpris2 definition',
      author='hugosenari',
      author_email='hugosenari@gmail.com',
      url='https://github.com/hugosenari/mpris2',
      keywords = ["dbus", "mpris2"],
      packages=('mpris2',),
      requires=('pydbusdecorator (>=1.0)', ),
      license = "GPL",
      classifiers=[
            "Development Status :: 4 - Beta",
            "Environment :: X11 Applications",
            "Intended Audience :: Developers",
            "License :: OSI Approved :: GNU General Public License (GPL)",
            "Programming Language :: Python :: 2.7",
            "Topic :: Software Development :: Libraries :: Python Modules",
      ],
      long_description = """\
====================================
Python usable definiton of MPRIS2
====================================

This is my lib to help developers work with Mpris2 and python

See Mpris2 site (http://www.mpris.org/2.1/spec/)

Require:
========

Python dbus and pydbusdecorator (https://github.com/hugosenari/pydbusdecorator)

Example:
========

Connect to player
-----------------

from mpris2.player.Player

from mpris2.some_players import Some_PLayers

uri = Interfaces.MEDIA_PLAYER + '.' + Some_PLayers.GMUSICBROWSER

# uri = 'org.mpris.MediaPlayer2.gmusicbrowser'

mp2 = Player(dbus_interface_info={'dbus_uri': uri})


Call methods
------------


mp2.Next() # play next media


Get attributes
--------------

print mp2.Metadata #current media data


Wait signal
-----------

from dbus.mainloop.glib import DBusGMainLoop

DBusGMainLoop(set_as_default=True)

import gobject    


def my_handler(self, Position):
    print 'handled', Position, type(Position)
    print 'self handled', self.last_fn_return, type(self.last_fn_return)


def another_handler(self, \*args, \*\*kw):
    print args, kw


mloop = gobject.MainLoop()

mp2.Seeked = my_handler

mp2.PropertiesChanged = another_handler

mloop.run()

""",
)