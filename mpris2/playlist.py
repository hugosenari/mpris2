from pydbusdecorator.dbus_data import DbusData

@DbusData()
class Playlist(object):
    '''
    A data structure describing a playlist.
    *Id — o (Playlist_Id)
        A unique identifier for the playlist.
        This should remain the same if the playlist is renamed.
    *Name — s
        The name of the playlist, typically given by the user.
    *Icon — s (Uri)
        The URI of an (optional) icon.
    '''
    def __init__(self, Id=None, Name=None, Icon=None):
        self._Id=Id
        self._Name=Name
        self._Icon=Icon
    
    @property
    def Id(self):
        return self._Id
    
    @property
    def Name(self):
        return self._Name
    
    @property
    def Icon(self):
        return self._Icon


@DbusData()
class Maybe_Playlist(Playlist):
    '''
    *Valid — b
        Whether this structure refers to a valid playlist.
    *Playlist — (oss) (Playlist)
        The playlist, providing Valid is true, otherwise undefined.
    When constructing this type, it should be noted that the playlist ID must be a valid object path, or D-Bus implementations may reject it. This is true even when Valid is false. It is suggested that "/" is used as the playlist ID in this case.
    '''
    
    def __init__(self, playlist=None):
        self._valid = True
        ## isn't none, copy playlist info
        if playlist != None:
            super(Maybe_Playlist, self).__init__(playlist.Id(), playlist.Name(), playlist.Icon())
        ## else ins't valid
        else:
            self._valid = False
    
    @property
    def Valid(self):
        return self._valid
    
    def __bool__(self):
        return self._valid