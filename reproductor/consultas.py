from .database import database

class consultas:

    def __init__(self):
        pass

    def get_rolas(self, to_search):
        self.to_search = to_search
        query = self.identify_query(self.to_search)
        word = self.to_search.split(",")
        longi = len(word)
        playlist = database()

        if(query == 1):
            titles = playlist.show_rolas_with_title([self.to_search.strip()])
            performers = playlist.show_rolas_with_performer([self.to_search.strip()])
            albums = playlist.show_rolas_with_album([self.to_search.strip()])
            genre = playlist.show_rolas_with_genre([self.to_search.strip()])
            titles.extend(performers)
            titles.extend(albums)
            titles.extend(genre)
            return titles
        if(query ==2):
            albums = playlist.show_rolas_with_album([word[1].strip()])
            return albums
        if(query == 3):
            titles = playlist.show_rolas_with_title([word[1].strip()])
            return titles
        if(query == 4):
            performers = playlist.show_rolas_with_performer([word[1].strip()])
            return performers
        if(query == 5):
            years = playlist.show_rolas_with_year([int(word[1])])
            return years;
        if(query == 10):
            genre = playlist.show_rolas_with_genre([word[1].strip()])
            return genre
        if(query == 6):
            albums = []
            i =0
            for elem in word:
                if(i != 0):
                    albums += playlist.show_rolas_with_album([elem.strip()])
                i += 1
            return albums;
        if(query == 7):
            songs=[]
            i= 0
            for elem in word:
                if(i != 0):
                    songs = songs.extend(playlist.show_rolas_with_title([elem.strip()]))
            return songs;
        if(query == 8):
            i= 0
            performers=[]
            for elem in word:
                if(i != 0):
                    performers += playlist.show_rolas_with_performer([elem.strip()])
            return performers;
        if(query == 9):
            i=0
            years =[]
            for elem in word:
                if(i != 0):
                    years += playlist.show_rolas_with_year([elem.strip()])
            return years
        if(query == 11):
            i= 0
            genre=[]
            for elem in word:
                if(i != 0):
                    genre += playlist.show_rolas_with_genre([elem.strip()])
            return genre

#Si la primera palabra es album: regr
    def identify_query(self, to_search):
        word = to_search.split(",")
        longi= len(word)
        if(longi == 1):
            return 1
        if(longi == 2 and word[0] == "album:"):
            return 2
        if(longi == 2 and word[0] == "song:"):
            return 3
        if(longi == 2 and word[0] == "performer:"):
            return 4
        if(longi == 2 and word[0] == "year:"):
            return 5
        if(longi > 2 and word[0] == "album:"):
            return 6
        if(longi > 2 and word[0] == "song:"):
            return 7
        if(longi > 2 and word[0] == "performer:"):
            return 8
        if(longi > 2 and word[0] == "year:"):
            return 9
        if(longi == 2 and word[0] == "genre:"):
            return 10
        if(longi > 2 and word[0] == "genre"):
            return 11
