from .base import Decorator

class DbusAttr(Decorator):
    """
    https://docs.python.org/2/howto/descriptor.html#properties
    """

    def __init__(self, meth=None, produces=lambda resp: resp):
        self.attr = meth
        self.produces = produces

    def __call__(self, meth):
        self.attr = meth
        return self
    
    def __get__(self, obj, objtype=None):
        #static call
        if not obj:
            return self

        props = obj._dbus_interface_info.properties
        iface = obj._dbus_interface_info.iface
        result = props.Get(iface, self.attr.__name__)
        produces = self.produces
        return produces(result)

    def __set__(self, obj, value):
        if obj:
            props = obj._dbus_interface_info.properties
            iface = obj._dbus_interface_info.iface
            props.Set(iface, self.attr.__name__, value)
        else: #static call
            self.attr = value

    def __delete__(self, obj):
        raise AttributeError("can't delete attribute")


if __name__ == '__main__':
    # examples
    from .interface import DbusInterface

    @DbusInterface('org.mpris.MediaPlayer2',
                   '/org/mpris/MediaPlayer2')
    class Example(object):
        @DbusAttr
        def Identity(self):
            pass

    d = Example(
        dbus_interface_info={
            'dbus_uri': 'org.mpris.MediaPlayer2.vlc'})

    assert d.Identity == 'VLC media player'