====================================
Python usable definiton of MPRIS2
====================================

This is my lib to help developers work with MPRIS2 and python

See Mpris2 site (http://specifications.freedesktop.org/mpris-spec/2.2/)

See also:
========

pympris (https://github.com/wistful/pympris)


Example:
========

Here is some examples, that shows how to work with this lib.


Configure dbus and mainloop
---------------------------

>>> # configure dbus and mainloop
>>> from dbus.mainloop.glib import DBusGMainLoop
>>> DBusGMainLoop(set_as_default=True)
>>> # old versions
>>> import gobject
>>> mloop = gobject.MainLoop()
>>> # python3
>>> import gi.repository.GLib
>>> mloop = gi.repository.GLib.MainLoop()


Discover your player dbus mpris uri
-----------------------------------

>>> # you can use get_players_uri to get current running players uri
>>> from mpris2 import get_players_uri
>>> print([uri for uri in get_players_uri()])
>>> uri = next(get_players_uri())
>>> # next raise StopIteration if not found
>>> # get_players_uri can be called with filter parameter
>>> # get_players_uri('.+rhythmbox')
>>>
>>> # you can set it yourself
>>> # uri = 'org.mpris.MediaPlayer2.gmusicbrowser'
>>>
>>> # you can use one predefined
>>> # from mpris2 import SomePlayers, Interfaces
>>> # uri = '.'.join([Interfaces.MEDIA_PLAYER, SomePlayers.GMUSICBROWSER])


Connect to player
-----------------

>>> # create you player
>>> from mpris2 import Player
>>> mp2 = Player(dbus_interface_info={'dbus_uri': uri})


Call methods
------------


>>> mp2.Next() # play next media


Get attributes
--------------

>>> print(mp2.Metadata) #current media data


Wait signal
-----------


>>> 
>>> def my_handler(self, Position):
>>>     print('handled', Position, type(Position))
>>>     print('self handled', self.last_fn_return, type(self.last_fn_return))
>>> 
>>> def another_handler(self, \*args, \*\*kw):
>>>     print(args, kw)
>>> 
>>> mp2.Seeked = my_handler
>>> 
>>> mp2.PropertiesChanged = another_handler
>>> 
>>> mloop.run()
