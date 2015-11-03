'''
This is not part of specification

Helper class to make it work as python lib
'''


class Decorator(object):
    def _update_me(self, target=None):
        if hasattr(target, "__doc__"):
            self.__doc__ = target.__doc__
        if hasattr(target, "__name__"):
            self.__name__ = target.__name__
        if hasattr(target, "__bases__"):
            self.__bases__ = target.__bases__
