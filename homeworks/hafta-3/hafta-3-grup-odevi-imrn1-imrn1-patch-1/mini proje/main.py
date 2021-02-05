from Library import Library
from UserDB import UserDB 


class Main:

    def show_student_menu(self):
        self.current_user.show_menu()

    def show_admin_menu(self):
        self.current_user.show_menu()

    def login(self,name,password):
        self.current_user = self.userDB.validate_user(name,password)

        if self.current_user == False:
            print("\nkullanıcı adı veya şifre hatalı!\n")
            return False
        else:
            # print(self.current_user.role)
            if self.current_user.role == "student":
                self.current_user.menu_flag=True
                self.show_student_menu()
            else:
                self.show_admin_menu()
   
   

    def __init__(self):
        self.library_flag = True
        self.userDB_flag = True
        self.userDB = UserDB()
        self.library = Library()
        self.current_user = None

          
        while True:
            y = self.login(input("name? ").strip(), input("\npassword? ").strip())
            if y!=False:
                break
       
        while True:
            x = input("cıkmak için 'e' ")
            if x == 'e':
                break 

    


main = Main()