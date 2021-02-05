from Book import Book

class Library(Book):

    example_books = {"001": ["Biology", 2, ["Alice", "Bob"]], "002": ["Chemistry", 3,["Alice"]]}

    author_to_book={}
    book_object={}
    example_books_flag=True
    
    
    
    def add_book(self,bid,name,copies,authors):
        obj=Book(bid,name,copies,authors)
        Library.book_object[bid]=[name,copies,authors]
        for i,j in self.book_object.items():
            s=""
            for a in j[2]:
                s+=a
            if i not in self.author_to_book:
                Library.author_to_book[s]=obj
                # print(i,j)
            else:
                Library.author_to_book[s]=obj
                # print(i,j)
    
    def create_example_book(self):
            for i,j in self.example_books.items():
                # print(i,j)
                self.add_book(i,j[0],j[1],j[2])

    def __init__(self):
        if Library.example_books_flag:
            self.create_example_book()
            Library.example_books_flag=False

    def remove_book(self,bid):
        for i,j in self.book_object.items():
            if i==bid:
                del i
                self.author_to_book.pop(j[2])
    def list_book(self):
        a=[]
        for i,j in self.book_object.items():
            a.append(j[0])
        return a
    def search_book(self,name = "",author=""):
        for i,j in Library.book_object.items():
            if j[0]==name or j[2] == author:
                return i

    def update_book_copies(self,copy,name="",author=""):
        Library.book_object[self.search_book(name = name,author=author)][1] =copy
