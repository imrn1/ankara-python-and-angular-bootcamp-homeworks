from Menu import Menu

class User:
    menu = Menu("")
    menu_items=[]
    def __init__(self,name,password):
        self.name=name 
        self.password=password

    def display(self):
        return self.name, self.password     

    def menu_builder(self):
        User.menu.menuItems = User.menu_items #!
        # User.menu.display(False)
    