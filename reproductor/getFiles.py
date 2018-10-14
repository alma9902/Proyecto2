from os import walk
from tags import tags
import os
class getFiles:
    files_list=[]
    paths_list=[]
    #lee recursivamente los archivos y directorios de ~/Music
    def __init__(self, ruta = './../../../../../root/Music-p/'):
        for(path, dirs, files) in walk(ruta):
            self.files_list.extend(files)
            for f in files:
                if len(f) != 0:
                    paths_s = ''.join(path)+f
                    self.paths_list.append(paths_s)
        self.files_list = sorted(self.files_list)
        self.paths_list = sorted(self.paths_list)
    def get_info(self):
        i=0
        for song in self.paths_list:
            info_song = tags(song)
            info_song.read_tags()
p = getFiles()
p.get_info()
