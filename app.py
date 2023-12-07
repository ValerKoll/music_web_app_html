import os
from flask import Flask, request, render_template
from lib.database_connection import get_flask_database_connection
from lib.album_repository import AlbumRepository
from lib.album import Album
from lib.artist_repository import ArtistRepository
from lib.artist import Artist

# Create a new Flask app
app = Flask(__name__)

# == Your Routes Here ==


# == Example Code Below ==

# GET /emoji
# Returns a smiley face in HTML
# Try it:
#   ; open http://localhost:5001/emoji
@app.route('/emoji', methods=['GET'])
def get_emoji():
    # We use `render_template` to send the user the file `emoji.html`
    # But first, it gets processed to look for placeholders like {{ emoji }}
    # These placeholders are replaced with the values we pass in as arguments
    return render_template('emoji.html', emoji=':)')
# == End Example Code ==


# ======== routes =============
#
@app.route('/albums', methods=['GET'])
def get_albums():
    #arg1 = request.args['all']
    sub_connection = get_flask_database_connection(app)
    albums_repo = AlbumRepository(sub_connection)
    albums = albums_repo.all()
    #text_to_return = [f"Title: {album.title}\nReleased: {album.release_year}"  for album in albums]
    #text_to_return = text_to_return[0] + text_to_return[1]
    print(albums)
    return render_template('albums.html', albums=albums)




@app.route('/albums', methods=['POST'])
def add_album():
    title = request.form['title']
    release_year = request.form['release_year']
    artist_id = request.form['artist_id']
    
    sub_connection = get_flask_database_connection(app)
    repo = AlbumRepository(sub_connection)
    #
    #
    repo.create(Album(1, title, release_year, artist_id))
    #
    albums = repo.all()
    response = ""
    for album in albums:
        response += f"{album}\n"
    return response
#
# ===============================
#
@app.route('/artists', methods=['GET'])
def get_artists():
    arg1 = request.args['all']
    sub_connection = get_flask_database_connection(app)
    artists_repo = ArtistRepository(sub_connection)
    artists = artists_repo.all()
    text_to_return = ""
    if arg1 == '1':
        for artist in artists:
            text_to_return += f"{artist}\n"
    elif arg1 == '2':
        text_to_return = ', '.join([artist.name for artist in artists])
    return text_to_return

@app.route('/artists', methods=['POST'])
def post_add_artist():
    arg1 = request.form['name']
    arg2 = request.form['genre']
    sub_connection = get_flask_database_connection(app)
    artists_repo = ArtistRepository(sub_connection)
    artists_repo.create(Artist(None, arg1, arg2))
    return ''
#
# ======== end rooutes ========

# ======== Challenge ========
@app.route('/albums/single_album/<int:id>', methods = ['GET'])
def get_single_album(id):
    sub_connection = get_flask_database_connection(app)
    albums_repo = AlbumRepository(sub_connection)
    artist_repo = ArtistRepository(sub_connection)
    album = albums_repo.find(id)
    artist = artist_repo.find(album.artist_id)
    print(id)
    return render_template('albums/single_album.html', album=album, artist=artist)


# These lines start the server if you run this file directly
# They also start the server configured to use the test database
# if started in test mode.
if __name__ == '__main__':
    app.run(debug=True, port=int(os.environ.get('PORT', 5001)))
