from MenuItem import MenuItem

class Menu:
    def __init__(self,header):
        self.header=header
        self.menuItems=[]
    
    def display(self,display_header):
        if display_header:
            print(self.header)
        print(self.menuItems)  #?   
        
        
    def add_menu_item(self,text,number):
        obj=MenuItem(text,number)
        self.menuItems.append(obj)
