'''
This is not part of specification

Helper class to make it work as python lib
'''

from functools import wraps
from .base import Decorator
from .interface import DbusInterface
from .attribute import DbusAttr

class DbusMethod(Decorator):
    pass


class DbusSignal(Decorator):
    pass
