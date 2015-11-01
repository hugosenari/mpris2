'''
utils functions not defined in espec
Created on Nov 6, 2011

@author: hugosenari
'''

import dbus, re
from .interfaces import Interfaces

def _match_players_uri(name, pattern='.+'):
    '''
        Filter logic for get_players and get_player_uri
        @param name: string name to test
        @param pattern=None:  string regexp to test
        @return: boolean
    '''
    return \
        re.match('org.mpris.MediaPlayer2', name)\
            and re.match(pattern, name)

def get_session():
    '''
        @return: dbus.SessionBus.get_session()
    '''
    return dbus.SessionBus.get_session()

def get_players_uri(pattern='.'):
    """
        Return string of player bus name
        @param pattern=None: string regex that filter response
        @return: array string of players bus name
    """
    return [item
        for item in get_session().list_names()
            if _match_players_uri(item, pattern)]

def get_player_id_from_uri(uri):
    """
        Returns player mpris2 id from uri
        @param uri: string mpris2 player dbus uri
        @return: string mrpis2 id
    """
    mateched = re.match(Interfaces.MEDIA_PLAYER + '\.(.+)', uri or '')
    return mateched.groups()[0]\
        if mateched\
        else ''

def get_players_id(pattern=None):
    """
        Return string of player mpris2 id
        @param pattern=None: string regex that filter response
        @return: array string of players bus name
    """
    for item in get_session().list_names():
        if _match_players_uri(item, pattern):
            yield get_player_id_from_uri(item)

if __name__ == '__main__':
    print('Running players:', get_players_uri())
    assert get_player_id_from_uri('org.mpris.MediaPlayer2.banshee') == 'banshee'
