'''
Audio Volume
'''
from pydbusdecorator.dbus_data import DbusData

@DbusData()
class Volume(object):
    '''
    Audio volume level
    *0.0 means mute.
    *1.0 is a sensible maximum volume level (ex: 0dB).
    Note that the volume may be higher than 1.0, although generally clients should not attempt to set it above 1.0.
    '''

    MIN = 0.0
    MAX = 1.0
    RANGE = set(range(0, 1, 0.1))
    
    def __init__(self, volume=1.0):
        self._volume = volume
        
    @property
    def volume(self):
        '''Get volume atrribute'''
        return self._volume

    def __get__(self, obj, objtype=None):
        return obj.volume if obj else self