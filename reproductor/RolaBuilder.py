""" Es el builder de la clase Rola, asigna a través
    de getters y setters el estado del objeto que
    queremos"""
from Rola import Rola

class RolaBuilder:

    def __init__(self):
        self.__song = Rola()
    def with_title(self, title):
       self.__song.set_title(title)
       return self
    def with_track(self, track):
       self.__song.set_track(track)
       return self
    def with_path(self, path):
       self.__song.set_path(path)
       return self
    def with_genre(self, genre):
       self.__song.set_genre(genre)
       return self
    def with_year(self, year):
        self.__song.set_year(year)
        return self
    def with_album(self, album):
        self.__song.set_album(album)
        return self
    def with_artist(self, artist):
        self.__song.set_artist(artist)
        return self
    def with_discnumber(self, discnumber):
        self.__song.set_discnumber(discnumber)
        return self
    def buildRola(self):
        if self.__song.valid_state():
            return self.__song
        else:
            print("no tiene los parámetros requeridos")
    def to_string_song(self):
        s = self.__song.get_title()+self.__song.get_genre()+self.__song.get_discnumber()+self.__song.get_year()+self.__song.get_track()+self.__song.get_artist()+self.__song.get_path()
        return s
