=======
Example
=======

Examples that shows how to work with this lib.



Connect to player
-----------------

>>> from mpris2.player.Player
>>> 
>>> from mpris2.some_players import Some_PLayers
>>> 
>>> uri = Interfaces.MEDIA_PLAYER + '.' + Some_PLayers.GMUSICBROWSER
>>> # uri = 'org.mpris.MediaPlayer2.gmusicbrowser'
>>> 
>>> mp2 = Player(dbus_interface_info={'dbus_uri': uri})


Call methods
------------


>>> mp2.Next() # play next media


Get attributes
--------------

>>> print mp2.Metadata #current media data


Wait signal
-----------

>>> from dbus.mainloop.glib import DBusGMainLoop
>>> 
>>> DBusGMainLoop(set_as_default=True)
>>> 
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
>>> mloop = gobject.MainLoop()
>>> 
>>> mp2.Seeked = my_handler
>>> 
>>> mp2.PropertiesChanged = another_handler
>>> 
>>> mloop.run()