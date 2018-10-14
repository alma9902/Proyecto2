from mutagen.mp3 import MP3
from mutagen.id3 import ID3NoHeaderError
from mutagen.id3 import ID3
from mutagen.easyid3 import EasyID3
from RolaBuilder import RolaBuilder


class tags:
    def __init__(self, path_song):
        self.audio = MP3(path_song, ID3=EasyID3)
        self.path_song = path_song

    def read_tags(self):
        song = RolaBuilder()
        song.with_title(self.audio['title'])
        song.with_artist(self.audio['artist'])
        song.with_path([self.path_song])
        song.with_discnumber(self.audio['discnumber'])
        song.with_track(self.audio['tracknumber'])
        song.with_genre(self.audio['genre'])
        song.with_year(self.audio['date'])
        print(song.to_string_song())
