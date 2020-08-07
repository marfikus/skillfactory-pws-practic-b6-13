
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
    
@route("/albums/", method="POST")
def add_new_album():
    # а если некоторые поля отсутствуют? тогда здеьсь надо проверять
    album = {
        # "id": request.forms.get("id"),
        "year": request.forms.get("year"),
        "artist": request.forms.get("artist"),
        "genre": request.forms.get("genre"),
        "album": request.forms.get("album")
    }
    
    # проверка корректности ввода
    valid_result = valid_data(album)
    if valid_result != "":
        return "Incorrect input! " + valid_result
        
    # проверка на существование такого альбома в бд
    
    
    # добавление альбома в бд
    

if __name__ == "__main__":
    run(host="localhost", port=8080, debug=True)