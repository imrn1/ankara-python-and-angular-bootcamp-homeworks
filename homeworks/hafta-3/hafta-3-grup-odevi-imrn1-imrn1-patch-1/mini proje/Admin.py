from User import User

class Admin(User):
    menu="Welcome to admin menu"
    menu_items= ["List books", "Create a book", "Delete a book","Search for a book","Change number of a copies of a book", "Show students borrowed a book by ""ID","List Users", "Create User","Delete User", "Exit"]
    # super().menu.header ="absds"  # bu yanlışş
    def __init__(self,name,password):
        super().__init__(name,password)
        self.role = "admin"
    
    def show_menu(self):
        User.menu.header = Admin.menu  # ... = self.menu de yazılabilir
        User.menu_items = self.menu_items
        super().menu_builder()  # class level olmadığı için super() ile erişim sağlandı
        User.menu.display(True)