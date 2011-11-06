from pydbusdecorator.dbus_data import DbusData

@DbusData()
class Uri(object):
    '''A unique resource identifier.'''
    def __init__(self, mstr):
        self._uri = mstr
    
    @property
    def uri(self):
        return self._uri
    
    def __str__(self):
        return self._uri
    
    def __cmp__(self, other):
        return self.uri() == str(other) if other != None else False