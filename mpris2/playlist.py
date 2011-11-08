class Playlist(object):
    '''
    A data structure describing a playlist.
    *Id - o (Playlist_Id)
        A unique identifier for the playlist.
        This should remain the same if the playlist is renamed.
    *Name - s
        The name of the playlist, typically given by the user.
    *Icon - s (Uri)
        The URI of an (optional) icon.
    '''
    def __init__(self, playlist):
        self._Id = playlist.get('Id')
        self._Name = playlist.get('Name')
        self._Icon = playlist.get('Icon')
    
    @property
    def Id(self):
        return self._Id
    
    @property
    def Name(self):
        return self._Name
    
    @property
    def Icon(self):
        return self._Icon

class Maybe_Playlist(Playlist):
    '''
    *Valid - b
        Whether this structure refers to a valid playlist.
    *Playlist - (oss) (Playlist)
        The playlist, providing Valid is true, otherwise undefined.
    When constructing this type, it should be noted that the playlist ID must be a valid object path, or D-Bus implementations may reject it. This is true even when Valid is false. It is suggested that "/" is used as the playlist ID in this case.
    '''
    
    def __init__(self, maybe_playlist=None):
        self._valid = maybe_playlist[0]
        ## isn't none, copy playlist info
        if maybe_playlist != None:
            super(Maybe_Playlist, self).__init__(maybe_playlist[1])
        ## else ins't valid
        else:
            self._valid = False
    
    @property
    def Valid(self):
        return self._valid
    
    def __bool__(self):
        return self._valid