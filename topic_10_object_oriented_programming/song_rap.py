class Song:
    def __init__(self, title="", author="", lyrics=()):
        self.title = title
        self.author = author
        self.lyrics = lyrics
        print(f"New Song made: {self.title} - {self.author}")

    # let's refactor out the printing of title and author
    def _print_title_author(self): # single underscore means it's a private method but can be used publicly if really needed
        if self.title and self.author:
            print(f"{self.title} - {self.author}")
 
    def sing(self, max_lines=-1):
        self._print_title_author()
        
        if max_lines == -1:  # Ja nav ierobežots rindiņu skaits, izdrukā visas
            # for line in self.lyrics:
            #     print(line)
            # we can set max_lines to be the length of the list
            max_lines = len(self.lyrics)
        # this way we avoid the use of else
        # for i in range(min(max_lines, len(self.lyrics))):
        #     print(self.lyrics[i])
        # no need to use index we can use slice which is more Pythonic
        for line in self.lyrics[:max_lines]: # remember that slice will not give us error if max_lines is bigger than the list
            print(line)
            # we could add a call to some Text-to-Speech library here
        
        return self  # Ķēdēšanai
 
    def yell(self, max_lines=-1):
        # Izdrukā dziesmu lielajiem burtiem ar rindiņām
        self._print_title_author()
        
        if max_lines == -1:  # Ja nav ierobežots rindiņu skaits, izdrukā visas
            for line in self.lyrics:
                print(line.upper())
        else:
            # for i in range(min(max_lines, len(self.lyrics))):
            #     print(self.lyrics[i].upper())
            # no need to use index we can use slice which is more Pythonic
            for line in self.lyrics[:max_lines]: # remember that slice will not give us error if max_lines is bigger than the list
                print(line.upper())
        return self  # Ķēdēšanai
    
# Četras papildu dziesmas
song1 = Song("Imagine", "John Lennon", ["Imagine there's no heaven", "It's easy if you try", "No hell below us", "Above us only sky"])

song2 = Song("Bohemian Rhapsody", "Queen", ["Is this the real life?", "Is this just fantasy?", "Caught in a landslide", "No escape from reality"])

# we have two song objects created from same Song class - template
song1.sing().yell(2)

song2.yell(3).sing(2)

# now let's create a rap song class that will inherit from Song class	

class Rap(Song):
    # custom __init__ method is not needed if we do not need to change the way the object is created
    # def __init__(self, title="", author="", lyrics=()):
    #     # Mantojam no Song klases
    #     super().__init__(title, author, lyrics)
    #    print(f"New Rap Song made: {self.title} - {self.author}")  # Pārdefinējam __init__ metodi
 
    def break_it(self, max_lines=-1, drop="yeah"):
        """
        Izdrukā dziesmu tekstu, pievienojot 'drop' vārdu pēc katra vārda.
        """
        self._print_title_author() # if we had used __print_title_author() it would not be accessible here
        # we then would need to unmangle the name _Song__print_title_author()
        
        if max_lines == -1:  # Ja nav ierobežots rindiņu skaits, izdrukā visas
            for line in self.lyrics:
                # Pievienojam 'drop' vārdu aiz katra vārda
                print(' '.join([f"{word} {drop}" for word in line.split()]))
        else:
            for i in range(min(max_lines, len(self.lyrics))):
                # Pievienojam 'drop' vārdu aiz katra vārda
                print(' '.join([f"{word} {drop}" for word in self.lyrics[i].split()]))
        
        return self  # Ķēdēšanai
    
song3 = Rap("Shape of You", "Ed Sheeran", ["The club isn't the best place to find a lover", "So the bar is where I go", "Me and my friends at the table doing shots", "Drinking fast and then we talk slow"])
song4 = Rap("Hotel California", "Eagles", ["On a dark desert highway, cool wind in my hair", "Warm smell of colitas, rising through the air", "Up ahead in the distance, I saw a shimmering light", "My head grew heavy and my sight grew dim"])

song3.break_it(2, "yo").sing(1)
song4.break_it(3, "ahem").yell(2)