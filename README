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

Here is some examples, that shows how to work with this lib.


Configure dbus and mainloop
---------------------------

>>> # configure dbus and mainloo
>>> from dbus.mainloop.glib import DBusGMainLoop
>>> DBusGMainLoop(set_as_default=True)
>>> import gobject
>>> mloop = gobject.MainLoop()


Discover your player dbus mpris uri
-----------------------------------

>>> # you can use get_players_uri to get current running players uri
>>> from mpris2.utils import get_players_uri
>>> print get_players_uri()
>>> if not get_players_uri(): raise Exception('No MPRIS2 players available, please start some player with mpris2.')
>>> uri = get_players_uri()[0] 
>>> # get_players_uri can be called with filter parameter
>>> # get_players_uri('.+rhythmbox')
>>>
>>> # you can set it yourself
>>> # uri = 'org.mpris.MediaPlayer2.gmusicbrowser'
>>>
>>> # you can use one predefined
>>> # from mpris2.some_players import Some_PLayers
>>> # uri = Interfaces.MEDIA_PLAYER + '.' + Some_PLayers.GMUSICBROWSER


Connect to player
-----------------

>>> # create you player
>>> from mpris2.player import Player
>>> mp2 = Player(dbus_interface_info={'dbus_uri': uri})


Call methods
------------


>>> mp2.Next() # play next media


Get attributes
--------------

>>> print mp2.Metadata #current media data


Wait signal
-----------


>>> import gobject
>>> 
>>> 
>>> def my_handler(self, Position):
>>>     print 'handled', Position, type(Position)
>>>     print 'self handled', self.last_fn_return, type(self.last_fn_return)
>>> 
>>> def another_handler(self, \*args, \*\*kw):
>>>     print args, kw
>>> 
>>> mp2.Seeked = my_handler
>>> 
>>> mp2.PropertiesChanged = another_handler
>>> 
>>> mloop.run()
