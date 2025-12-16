"""
8. Implement __add__. Create a class where adding two objects with + produces a 
new combined object.  

"""
class Playlist:
    def __init__(self,songs):
        self.songs = songs

    def __add__(self,other):
        if not isinstance(other,Playlist):
            return NotImplemented
        return Playlist(self.songs + other.songs)
    
p1 = Playlist(["Song 1", "Song 2"])
p2 = Playlist(["Song 3" ,"Song 4"])

p3 = p1 + p2
print(p3.songs)
