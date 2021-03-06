
import sqlalchemy as sa
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

DB_PATH = "sqlite:///albums.sqlite3"
Base = declarative_base()

class Album(Base):
    __tablename__ = "album"
    
    id = sa.Column(sa.INTEGER, primary_key=True)
    year = sa.Column(sa.INTEGER)
    artist = sa.Column(sa.TEXT)
    genre = sa.Column(sa.TEXT)
    album = sa.Column(sa.TEXT)
    
def connect_db():
    # создаём подключение к бд
    engine = sa.create_engine(DB_PATH)
    # создаём описанные таблицы
    Base.metadata.create_all(engine)
    # создаём фабрику сессий
    Sessions = sessionmaker(engine)
    # создаём сессию
    session = Sessions()
    return session
    
def find(artist):
    session = connect_db()
    
    albums = session.query(Album).filter(Album.artist == artist).all()
    return albums
    
def check_on_exists(album):
    session = connect_db()
    
    albums = session.query(Album).filter(
        Album.album == album["album"],
        Album.artist == album["artist"],
        Album.year == album["year"]
    ).all()

    if not albums:
        return True
    
    return False

def valid_input_data(album):
    MAX_LENGTH = 150
    
    if album["year"] is None:
        return "Field 'Year' is missing"
    year = str(album["year"])
    if len(year) < 4:
        return "Length of field 'Year' less than 4 characters"
    if len(year) > 4:
        return "Length of field 'Year' more than 4 characters"
    try:
        year = int(year)
    except ValueError:
        return "Field 'Year' is not a number"
    if year < 0:
        return "Field 'Year' is negative number"
   
    if album["artist"] is None:
        return "Field 'Artist' is missing"
    if album["artist"].strip() == "":
        return "Field 'Artist' is empty"
    if len(album["artist"]) > MAX_LENGTH:
        return "Length of field 'Artist' more than {} characters".format(MAX_LENGTH)
        
    if album["genre"] is None:
        return "Field 'Genre' is missing"
    if album["genre"].strip() == "":
        return "Field 'Genre' is empty"
    if len(album["genre"]) > MAX_LENGTH:
        return "Length of field 'Genre' more than {} characters".format(MAX_LENGTH)
        
    if album["album"] is None:
        return "Field 'Album' is missing"
    if album["album"].strip() == "":
        return "Field 'Album' is empty"
    if len(album["album"]) > MAX_LENGTH:
        return "Length of field 'Album' more than {} characters".format(MAX_LENGTH)
    
    return ""
    
def add(album):
    session = connect_db()
    
    new_album = Album(
        year=album["year"], 
        artist=album["artist"], 
        genre=album["genre"], 
        album=album["album"]
    )    
    session.add(new_album)
    session.commit()
    