from os import walk
from tags import tags
import os
class getFiles:

    paths_list=[]
    album_path_list=[]
    #lee recursivamente los archivos y directorios de ~/Music
    def __init__(self, ruta = './../../../../../root/Music-p/'):
        for(path, dirs, files) in walk(ruta):
            for f in files:
                if len(f) != 0:
                    album_path = ''.join(path)+"/"
                    self.album_path_list.append(album_path)
                    paths_s = ''.join(path)+"/"+f
                    self.paths_list.append(paths_s)
        self.album_path_list = sorted(self.album_path_list)
        self.paths_list = sorted(self.paths_list)
    def get_info(self):
        i=0
        for song in self.paths_list:
            info_song = tags(song, self.album_path_list[i])
            info_song.read_tags()
            info_song.send_minar()
            i += 1
p = getFiles()
p.get_info()
