
from bottle import run
from bottle import route
from bottle import HTTPError
# from bottle import request

import albums_finder

@route("/")
def it_works():
    return "It works!"

@route("/albums/<artist>")
def albums(artist):
    albums_list = finder.find(artist)
    
    if not albums_list:
        message = "Albums '{}' not found".format(artist)
        result = HTTPError(404, message)
    else:
        album_names = [album.album for album in albums_list]
        result = "Albums of '{}':<br>".format(artist)
        result += "<br>".join(album_names)
    return result

if __name__ == "__main__":
    run(host="localhost", port=8080, debug=True)