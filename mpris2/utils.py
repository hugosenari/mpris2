'''
utils functions not defined in espec
'''

import dbus, re

from .interfaces import Interfaces

def _match_players_uri(name, pattern='.+'):
    '''
        Filter logic for get_players and get_player_uri
        @param name: string name to test
        @param pattern=None:  string RegEx to test
        @return: boolean
    '''
    return \
        re.match('org.mpris.MediaPlayer2', name)\
            and re.match(pattern, name)

def get_session():
    '''
        @return: dbus.SessionBus.get_session()
    '''
    return dbus.SessionBus.get_session()

def get_players_uri(pattern='.'):
    '''
        Return string of player bus name
        @param pattern=None: string RegEx that filter response
        @return: array string of players bus name
    '''
    for item in get_session().list_names():
        if _match_players_uri(item, pattern):
            yield item


def get_player_id_from_uri(uri):
    '''
        Returns player mpris2 id from uri
        @param uri: string mpris2 player dbus uri
        @return: string mrpis2 id
    '''
    mateched = re.match(Interfaces.MEDIA_PLAYER + '\.(.+)', uri or '')
    return mateched.groups()[0]\
        if mateched\
        else ''

def get_players_id(pattern=None):
    '''
        Return string of player mpris2 id
        @param pattern=None: string RegEx that filter response
        @return: array string of players bus name
    '''
    for item in get_session().list_names():
        if _match_players_uri(item, pattern):
            yield get_player_id_from_uri(item)

def get_mainloop():
    try:
        from dbus.mainloop.glib import DBusGMainLoop
        DBusGMainLoop(set_as_default=True)
        try:
            import gobject
            return gobject.MainLoop()
        except:
            pass
         
        try:
            import gi.repository.GLib
            return gi.repository.GLib.MainLoop()
        except:
            pass
    except:
        pass
    
    class PyQtMainLoop():
        def __init__(self, app):
            self.app = app
        
        def run(self):
            if hasattr(self.app, 'exec_'):
                self.app.exec_()
            if hasattr(self.app, 'exec'):
                method = getattr(self.app, 'exec')
                method(self.app)

    
    try:
        from dbus.mainloop.qt import DBusQtMainLoop
        DBusQtMainLoop(set_as_default=True)
        try:
            from PySide.QtGui import QApplication
            return PyQtMainLoop(QApplication([]))
        except:
            pass
    
        try:
            from PyQt5.QtWidgets import QApplication  
            return PyQtMainLoop(QApplication([]))
        except:
            pass
    
        try:
            from PyQt4 import Qt
            return PyQtMainLoop(Qt.QApplication([]))
        except:
            pass
    except:
        pass

    return None

def list_interfaces(uri, path=None, bus=None):
    path = path or Interfaces.OBJECT_PATH
    import xml.etree.ElementTree as ET
    
    bus = bus or dbus.SessionBus.get_session()
    obj = bus.get_object(uri, path)
    node = ET.fromstring(obj.Introspect(dbus_interface='org.freedesktop.DBus.Introspectable'))    
    for interface in node.findall('interface'):
        yield interface.attrib['name']
        
def implements(uri, interface, path=Interfaces.OBJECT_PATH, bus=None):
    for iface in list_interfaces(uri, path, bus):
        if iface == interface:
            return True


if __name__ == '__main__':
    uris = get_players_uri()
    if not uris:
        print('No running players')
    for uri in uris:
        print(uri, ':')
        for interface in list_interfaces(uri):
            print('\t', interface)
