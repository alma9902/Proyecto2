""" Esta clase será instanciada por un builder
    para que el objeto tenga sus atributos correspondientes
    según los datos del mp3"""
class Rola:
    def __init__(self):
        pass
    #getters y setters correspondientes
    def set_title(self, title):
        self.__title= title
    def get_title(self):
        return self.__title

    def set_track(self,track):
        self.__track = track
    def get_track(self):
        return self.__track

    def set_genre(self, gender):
        self.__genre = gender
    def get_genre(self):
        return self.__genre

    def set_year(self, year):
        self.__year = year
    def get_year(self):
        return self.__year

    def set_path(self, path):
        self.__path = path

    def get_path(self):
        return self.__path

    def set_album(self, album):
        self.__album= album

    def get_album(self):
        return self.__album

    def set_album_path(self, album_path):
        self.__album_path = album_path

    def get_album_path(self):
        return self.__album_path
    def set_artist(self, artist):
        self.__artist= artist

    def get_artist(self):
        return self.__artist

    def set_discnumber(self, discnumber):
        self.__discnumber= discnumber
    def get_discnumber(self):
        return self.__discnumber

    def valid_state(self):
        condition = self.__title != ""
        condition = condition and self.__track != ""
        condition = condition and self.__genre != ""
        condition = condition and self.__year != ""
        condition = condition and self.__path != ""
        return condition
