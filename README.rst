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

>>> # configure mainloop (not required if you wont expect signals)
>>> from dbus.mainloop.glib import DBusGMainLoop
>>> DBusGMainLoop(set_as_default=True)


Discover your player mpris uri 
------------------------------

>>> # you can use get_players_uri to get current running players uri
>>> from mpris2 import get_players_uri
>>> # next raise StopIteration if not found
>>> uri = next(get_players_uri())


Connect to player
-----------------

>>> # create you player
>>> from mpris2 import Player
>>> player = Player(dbus_interface_info={'dbus_uri': uri})


Call methods
------------


>>> player.Next() # play next media


Get attributes
--------------

>>> print(player.Metadata) #current media data


Wait signal
-----------


>>> def another_handler(self, *args, **kw):
>>>     print(args, kw)
>>> 
>>> player.PropertiesChanged = another_handler
>>> # python3
>>> import gi.repository.GLib
>>> mloop = gi.repository.GLib.MainLoop()
>>> mloop.run()


Other examples:
---------------

>>> # old versions mainloop
>>> import gobject
>>> mloop = gobject.MainLoop()

>>> # list all running players
>>> from mpris2 import get_players_uri
>>> print([uri for uri in get_players_uri()])
>>> # get_players_uri can be called with filter parameter
>>> get_players_uri('.+rhythmbox')
>>> # you can set it yourself
>>> uri = 'org.mpris.MediaPlayer2.gmusicbrowser'
>>> # or use one predefined
>>> from mpris2 import SomePlayers, Interfaces
>>> uri = '.'.join([Interfaces.MEDIA_PLAYER, SomePlayers.GMUSICBROWSER])

>>> # test other interfaces
>>> from mpris2 import MediaPlayer2
>>> mp2 = MediaPlayer2(dbus_interface_info={'dbus_uri': uri})
>>> # not all players implement this:
>>> from mpris2 import Playlists, TrackList
>>> pls = Playlists(dbus_interface_info={'dbus_uri': uri})
>>> tl = TrackList(dbus_interface_info={'dbus_uri': uri})
