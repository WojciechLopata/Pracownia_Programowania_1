class book():
    def __init__(self,author,genre,year):
        self.author=author
        self.genre=genre
        self.year=year
    def display(self):
        print(vars(self))
class e_book(book):
    def __init__(self,author,genre,year,file):
        book.__init__(self,author,genre,year)
        self.file=file
class p_book(book):
    def __init__(self,author,genre,year,pages):
        book.__init__(self,author,genre,year)
        self.pages=pages
        
        
book_1=e_book("tolkine","fantasy","1994","plik.jpg")
book_2=p_book("rowling","fantasy","2013","123")
book_1.display()
book_2.display()