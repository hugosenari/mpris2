from pydbusdecorator.dbus_data import DbusData

@DbusData()
class Loop_Status(object):
    '''
    A repeat / loop status
    *None (None)
        The playback will stop when there are no more tracks to play
    *Track (Track)
        The current track will start again from the begining once it has finished playing
    *Playlist (Playlist)
        The playback loops through a list of tracks
    '''
    NONE = None
    TRACK = 'Track'
    PLAYLIST = 'Playlist'
    
    def __init__(self, mstr):
        self._status = mstr
    
    @property
    def status(self):
        return self._status
    
    def __str__(self):
        return self.status
    
    def __get__(self, obj, objtype=None):
        return obj.status if obj else self