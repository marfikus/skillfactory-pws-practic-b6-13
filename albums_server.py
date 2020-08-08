
from bottle import run
from bottle import route
from bottle import HTTPError
from bottle import request

import albums_finder
import add_album

@route("/")
def it_works():
    return "It works!"

@route("/albums/<artist>")
def albums(artist):
    albums_list = albums_finder.find(artist)
    
    if not albums_list:
        message = "Albums '{}' not found".format(artist)
        result = HTTPError(404, message)
    else:
        album_names = [album.album for album in albums_list]
        result = "{} album(s) of '{}':<br>".format(len(album_names), artist)
        result += "<br>".join(album_names)
    return result
    
@route("/albums", method="POST")
def add_new_album():
    album = {
        # "id": request.forms.get("id"),
        "year": request.forms.get("year"),
        "artist": request.forms.get("artist"),
        "genre": request.forms.get("genre"),
        "album": request.forms.get("album")
    }
    
    # проверка корректности ввода
    valid_result = add_album.valid_input_data(album)
    if valid_result != "":
        message = "Incorrect input! " + valid_result
        return HTTPError(400, message)

    # проверка на существование такого альбома в бд
    if not albums_finder.check_on_exists(album):
        message = "This album is alredy exists in the database!"
        return HTTPError(409, message)
    
    # добавление альбома в бд
    add_album.add_album(album)
    return "Album added"

if __name__ == "__main__":
    run(host="localhost", port=8080, debug=True)