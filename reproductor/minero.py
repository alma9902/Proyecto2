from RolaBuilder import RolaBuilder
from Rola import Rola
from Database import Database
from pprint import pprint


class minero:
    def __init__(self, song):
        self.__song = song.get_rola()

    def seed_database(self):
        path= ''.join(self.__song.get_path())
        title = ''.join(self.__song.get_title())
        track = ''.join(self.__song.get_track())
        year = ''.join(self.__song.get_year())
        album_name = ''.join(self.__song.get_album())
        album_path = ''.join(self.__song.get_album_path())
        performer_name = ''.join(self.__song.get_artist())
        #pprint(performer_name)
        song_to_save = Database()
        id_performer = song_to_save.check_performers([performer_name])
        if (len(id_performer) == 0):
            song_to_save.insert_in_performers([performer_name])
        #song_to_save.insert_in_rola([(path),(title),(track),(int(year))],[(album_path),(album_name),(int(year))])
