"""Se encarga de la conexión con la base de datos
    y de hacer las querys correspondientes"""
import sqlite3
from pprint import pprint
class Database:

    def __init__(self):
        pass

    def insert_in_rola(self,data, dataAlbum):
        conn = sqlite3.connect('./../../../../../root/rolas.db')
        db = conn.cursor()
        try:
                db.execute("insert into rolas ( path, title, track, year) values (?,?,?,?)",data)
                db.execute("insert into albums(path, name, year) values (?,?,?)",dataAlbum)
                conn.commit()
        except sqlite3.IntegrityError:
            print('el registro ya existe')
        finally:
            conn.close()

    def insert_in_performers(self,data):
        conn = sqlite3.connect('./../../../../../root/rolas.db')
        db = conn.cursor()
        db.execute("insert into performers (name) VALUES (?)",data)

    def check_performers(self, name):
        conn = sqlite3.connect('./../../../../../root/rolas.db')
        db = conn.cursor()
        db.execute("select id from performers where name = (?)",name)
        result = self.db.fetchall()
        return result

    def query_result(self,query):
        pprint(query)
        #db.execute("insert into rolas (path, title) values (?)",query)
        #ok = db.fetchall()
        db.close()
        return ok
