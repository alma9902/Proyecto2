"""Se encarga de la conexión con la base de datos
    y de hacer las querys correspondientes"""
import sqlite3
from pprint import pprint
class Database:

    def __init__(self):
        pass

    def insert_in_rola(self,data):
        conn = sqlite3.connect('./../../../../../root/rolas.db')
        db = conn.cursor()
        try:
                db.execute("insert into rolas ( id_performer, id_album, path, title, track, year, genre) values (?,?,?,?,?,?,?)",data)
                conn.commit()
        except sqlite3.IntegrityError:
            print('el registro ya existe')
        finally:
            conn.close()

    def insert_in_performers(self,data):
        conn = sqlite3.connect('./../../../../../root/rolas.db')
        db = conn.cursor()
        db.execute("insert into performers (name,id_type) VALUES (?,?)",data)
        conn.commit()
        conn.close()

    def insert_in_albums(self,data):
        conn = sqlite3.connect('./../../../../../root/rolas.db')
        db = conn.cursor()
        db.execute("insert into albums (path, name, year) VALUES (?,?,?)",data)
        conn.commit()
        conn.close()

    #Devuelve el id del performer según su nombre
    def check_performers(self, name):
        conn = sqlite3.connect('./../../../../../root/rolas.db')
        db = conn.cursor()
        rows = db.execute("select id_performer from performers where name = (?)",name)
        return rows.fetchone()
        return rows.fetchone()

    #Devuelve el id del album según su nombre
    def check_albums(self, name):
        conn = sqlite3.connect('./../../../../../root/rolas.db')
        db = conn.cursor()
        rows =db.execute("select id_album from albums where name = (?)",name)
        return rows.fetchone()

    #Recibe datos de la canción y retorna la canción si todos sus datos son iguales
    def check_rolas(self,data):
        conn = sqlite3.connect('./../../../../../root/rolas.db')
        db = conn.cursor()
        rows = db.execute("select * from rolas where id_performer = (?) and id_album = (?) and path = (?) and title=(?) and track=(?) and year=(?) and genre=(?)",data)
        return rows.fetchone()


    # Regresa el título de la rola, el performer, el album, el track,
    # el año y el genre
    def show_rolas(self) :
        conn = sqlite3.connect('./../../../../../root/rolas.db')
        db = conn.cursor()
        rows = db.execute("select title, performers.name, albums.name, track, rolas.year, genre from rolas INNER JOIN performers INNER JOIN albums")
        return rows.fetchall() is not None

    def show_rolas_with_performer(self, name):
         conn = sqlite3.connect('./../../../../../root/rolas.db')
         db = conn.cursor()
         rows = db.execute("select title, performers.name, albums.name, track, rolas.year, genre from rolas INNER JOIN performers INNER JOIN albums where performers.name = (?)",name)
         return rows.fetchall() is not None

    def show_rolas_with_title(self, title):
         conn = sqlite3.connect('./../../../../../root/rolas.db')
         db = conn.cursor()
         rows = db.execute("select title, performers.name, albums.name, track, rolas.year, genre from rolas INNER JOIN performers INNER JOIN albums where rolas.title = (?)",title)
         return rows.fetchall() is not None

    def show_rolas_with_year(self, year):
         conn = sqlite3.connect('./../../../../../root/rolas.db')
         db = conn.cursor()
         rows = db.execute("select title, performers.name, albums.name, track, rolas.year, genre from rolas INNER JOIN performers INNER JOIN albums where rolas.year = (?)",year)
         return rows.fetchall() is not None

    def show_rolas_with_genre(self, genre):
         conn = sqlite3.connect('./../../../../../root/rolas.db')
         db = conn.cursor()
         rows = db.execute("select title, performers.name, albums.name, track, rolas.year, genre from rolas INNER JOIN performers INNER JOIN albums where rolas.genre = (?)",genre)
         return rows.fetchall() is not None

    def show_rolas_with_album(self, name):
          conn = sqlite3.connect('./../../../../../root/rolas.db')
          db = conn.cursor()
          rows = db.execute("select title, performers.name, albums.name, track, rolas.year, genre from rolas INNER JOIN performers INNER JOIN albums where albums.name = (?)",name)
          return rows.fetchall() is not None
