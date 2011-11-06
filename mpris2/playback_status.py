from pydbusdecorator.dbus_data import DbusData

@DbusData()
class Playback_Status(object):
    '''
    A playback state.
    *Playing (Playing)
        A track is currently playing.
    *Paused (Paused)
        A track is currently paused.
    *Stopped (Stopped)
        There is no track currently playing.
    '''
    PLAYING = 'Playing'
    PAUSED = 'Paused'
    STOPPED = 'Stopped'
    
    def __init__(self, mstr):
        self._status = mstr
    
    @property
    def status(self):
        return self._status
    
    def __get__(self, obj, objtype=None):
        return obj.status if obj else self