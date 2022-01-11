class Music():
    def __init__(self,performer,song_name,album_name,year_of_release):
        self.perfromer=performer
        self.name=song_name
        self.album=album_name
        self.year=year_of_release
    def __str__(self):
        return "Perfomer:"+ self.perfromer+"\n"+"Song: "+self.name+"\n"+"album: "+self.album+"\nYear: "+self.year
test=Music("Ed","Ginger coś tam","Album nr 3","2018")
print(test)