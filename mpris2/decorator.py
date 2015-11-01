class Decorator(object):    
    def __init__(self, *args, **kwds):
        pass

    def __call__(self, arg):
        return arg

    

class DbusAttr(Decorator):
    pass


class DbusInterface(Decorator):
    pass


class DbusMethod(Decorator):
    pass


class DbusSignal(Decorator):
    pass