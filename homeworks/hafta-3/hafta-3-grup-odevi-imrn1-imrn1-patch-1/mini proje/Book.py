
class Book:
    def __init__(self,bid,name,no_of_copies,list_of_authors):
        self.bid=bid
        self.name=name
        self.no_of_copies=no_of_copies
        self.list_of_authors=list_of_authors
    def display(self):
        return self.bid,self.name,self.no_of_copies,self.list_of_authors
