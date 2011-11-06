from pydbusdecorator.dbus_data import DbusData

@DbusData()
class Playback_Rate(object):
    '''
    A playback rate
    This is a multiplier,
    so a value of 0.5 indicates that playback is happening at half speed,
    while 1.5 means that 1.5 seconds of "track time" is consumed every second.
    '''
    def __init__(self, rate=1.0):
        self._rate = rate
        
    @property
    def rate(self):
        return self._rate
    
    def __get__(self, obj, objtype=None):
        return obj.rate if obj else self