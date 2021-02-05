from User import User

class Student(User):
    menu_flag=False
    menu = "Welcome to student menu"
    menu_items = ["Search for a book", "Add a book to my book list", "delete a bookfrom my book list","show my borrowed books", "Exit"]
    def __init__(self,name,password):
        super().__init__(name,password)
        self.role = "student"
        if self.menu_flag:
            self.show_menu()

    def show_menu(self):
        User.menu.header = Student.menu
        User.menu_items = Student.menu_items
        super().menu_builder()  # class level olmadığı için super() ile erişim sağlandı
        Student.menu_flag = False # ? olmalı mı
        User.menu.display(True)