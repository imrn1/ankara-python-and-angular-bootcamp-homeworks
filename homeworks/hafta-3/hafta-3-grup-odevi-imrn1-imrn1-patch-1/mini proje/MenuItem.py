class MenuItem:
    def __init__(self,text,number):
        self.text=text
        self.number=number
    
    def display(self):
        return self.number,self.text
