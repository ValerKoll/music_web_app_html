#import pytest
from lib.album import Album
#from database_connection import DatabaseConnection




class AlbumRepository():
    def __init__(self, connection):
        self._connection = connection
    
    def all(self):
        rows = self._connection.execute("SELECT * FROM albums")
        ab = []
        for row in rows:
            item = Album(row["title"], row["release_year"], row["artist_id"])
            ab.append(item)
        return ab
    
    def find(self, album_id):
        rows = self._connection.execute(
            'SELECT * FROM albums WHERE id = %s', [album_id])
        row = rows[0]
        return Album(row["title"], row["release_year"], row["artist_id"])

#db_connection.seed("seeds/music_library_addtable.sql")
#a = AlbumRepository(db_connection())
#print(a.all()[0].title)