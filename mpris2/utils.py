'''
utils functions not defined in espec
Created on Nov 6, 2011

@author: hugosenari
'''

import dbus, re

def get_session():
    '''
        @return: dbus.SessionBus.get_session()
    '''
    return dbus.SessionBus.get_session()

def get_players_uri(pattern=None):
    """
        Return string of player bus name
        @param pattern=None: string regexo that filter response
        @return: array string of players bus name
    """
    return [item
        for item in get_session().list_names()
            if _match_players_uri(item, pattern)]


def _match_players_uri(name, pattern=None):
    '''
        Filter logic for get_players and get_player_uri
        @param name: string name to test
        @param pattern=None:  string regexp to test
        @return: boolean
    '''
    mpattern = 'org.mpris.MediaPlayer2'
    if pattern == None:
        return re.match(mpattern, name) > 0
    else:
        return re.match(pattern, name) > 0 and re.match(mpattern, name) > 0

if __name__ == '__main__':
    print get_players_uri()