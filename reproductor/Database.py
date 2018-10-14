"""Se encarga de la conexión con la base de datos
    y de hacer las querys correspondientes"""
import sqlite3
class DataBase:

    def insert_in(self,query):
        conn = sqlite3.connect('./../../../../../root/rolas.db')
        db = conn.cursor()
        try:
                db.execute(query)
                conn.commit()
        except sqlite3.IntegrityError:
            print('el registro ya existe')
        finally:
            conn.close()
    def query_result(self,query):
        conn = sqlite3.connect('./../../../../../root/rolas.db')
        db = conn.cursor()
        db.execute(query)
        ok = db.fetchall()
        db.close()
        return ok
    

datos = DataBase()
#datos = datos.connection()
datos.insert_in("INSERT INTO rolas (id_performer, id_album, path, title, track, year, genre)VALUES (081349812, 91234093128, '~/Music/A/rolling in the deep', 'rolling in the deep',8329, 2012, 'pop')")
print(datos.query_result("SELECT * FROM rolas"))
#datos.insert_in("INSERT INTO rolas (id_performer, id_album, path, title, track, year, genre)VALUES (081349812, 91234093128, '~/Music/A/rolling in the deep', 'rolling in the deep',8329, 2012, 'pop')")
