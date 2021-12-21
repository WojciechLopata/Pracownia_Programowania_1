class e_book():
    def __init__(self,title,author,page_num,curr_page):
        self.title=title
        self.author=author
        self.page_num=page_num
        #poniższe jest bo ktoś może mieć zakładke i czytac na kilka razy
        self.curr_page=curr_page
        self.is_open=False
    def e_b_close(self):
        self.is_open=False
    def e_b_open(self):
        self.is_open=True
    def display(self):
        print("title:'",self.title,"autor:",self.author,"page number:",self.page_num,"current page",self.curr_page)
    
    def read(self):
        if(self.is_open):
            self.curr_page+=1
book=e_book("harry potter","A.hawking",132,1)
e_book.e_b_open(book)
e_book.display(book)
e_book.read(book)
e_book.read(book)
e_book.read(book)
e_book.read(book)
e_book.read(book)
e_book.display(book)
e_book.e_b_close(book)
e_book.read(book)
e_book.read(book)
e_book.read(book)
e_book.display(book)


