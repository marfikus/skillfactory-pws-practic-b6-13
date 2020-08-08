
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