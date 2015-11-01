class Time_In_Us(int):
    '''Time in microseconds.'''
    
    def __init__(self, time=0):
        self._time = time
    
    def __int__(self):
        return int(self._time)
    
    def __str__(self):
        return str(self._time)


if __name__ == "__main__":
    assert Time_In_Us(10) == 10
