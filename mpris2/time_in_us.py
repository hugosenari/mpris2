'''
Created on Nov 5, 2011

@author: hugosenari
'''
from pydbusdecorator.dbus_data import DbusData

@DbusData()
class Time_In_Us(object):
    '''Time in microseconds.'''
    
    def __init__(self, time=0):
        '''constructor'''
        self._time = time
        
    @property
    def time(self):
        '''get time value'''
        return self._time

    def __get__(self, obj, objtype=None):
        return obj.time if obj else self