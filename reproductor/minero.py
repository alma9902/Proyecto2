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
        genre = ''.join(self.__song.get_genre())
        album_name = ''.join(self.__song.get_album())
        album_path = ''.join(self.__song.get_album_path())
        performer_name = ''.join(self.__song.get_artist())
        #pprint(performer_name)
        song_to_save = Database()
        self.id_performer = song_to_save.check_performers([performer_name])
        self.id_album = song_to_save.check_albums([album_name])
        self.rola = ""
        if( self.id_performer is not None ):
            if( self.id_album is not None):
                self.rola=song_to_save.check_rolas([(self.id_performer[0]),(self.id_album[0]),(path),(title),(track),(int(year)),(genre)])
        pprint(self.id_performer)
        pprint(self.id_album)
        #pprint(self.rola)

        if (self.id_performer is None):
            song_to_save.insert_in_performers([(performer_name),(2)])
            self.id_performer = song_to_save.check_performers([performer_name])

        if(self.id_album is None):
            song_to_save.insert_in_albums([(album_path),(album_name),(year)])
            self.id_album = song_to_save.check_albums([album_name])

        if(self.rola != "" and self.rola is None):
            song_to_save.insert_in_rola([(self.id_performer[0]),(self.id_album[0]),(path),(title),(track),(int(year)),(genre)])
            self.rola=self.rola = song_to_save.check_rolas([(self.id_performer[0]),(self.id_album[0]),(path),(title),(track),(int(year)),(genre)])
