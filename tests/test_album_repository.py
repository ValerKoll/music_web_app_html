from lib.album_repository import AlbumRepository
from lib.album import Album

"""
test, 1900, 1

When we call AlbumRepository # all
We get a list of Album objects reflecting the seed data.    
"""
def test_get_all_records(db_connection):
    db_connection.seed("seeds/music_library.sql")
    repository = AlbumRepository(db_connection)
    
    result = repository.all()
    
    assert result == [
        Album('Doolittle', 1989, 1),
        Album('Surfer Rosa', 1988, 1),
        Album('Waterloo', 1974, 2),
        Album('Super Trouper', 1980, 2)
        ]
