class Playlist_Id(str):
    '''
    Unique playlist identifier.
    '''

    def __init__(self, playlist_id):
        self._playlist_id = playlist_id
    
    def __str__(self):
        return self._status


if __name__ == "__main__":
    pid = Playlist_Id("id of a playlist")
    assert pid == "id of a playlist"
