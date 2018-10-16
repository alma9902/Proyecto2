from mutagen.mp3 import MP3
from mutagen.id3 import ID3NoHeaderError
from mutagen.id3 import ID3
from mutagen.easyid3 import EasyID3
from RolaBuilder import RolaBuilder
from minero import minero


class tags:
    def __init__(self, path_song, album_path):
        self.audio = MP3(path_song, ID3=EasyID3)
        self.path_song = path_song
        self.album_path = album_path

    def read_tags(self):
        self.song = RolaBuilder()
        self.song.with_title(self.audio['title'])
        self.song.with_artist(self.audio['artist'])
        self.song.with_path([self.path_song])
        self.song.with_discnumber(self.audio['discnumber'])
        self.song.with_track(self.audio['tracknumber'])
        self.song.with_genre(self.audio['genre'])
        self.song.with_year(self.audio['date'])
        self.song.with_album(self.audio['album'])
        self.song.with_album_path([self.album_path])
        self.song.to_string_song()

    def send_minar(self):
        llenar= minero(self.song)
        llenar.seed_database()
