class chatbook:
    # Defining the attributes of the class
    def __init__(self):
        self.username = ''
        self.password = ''
        self.loggedin = False
        self.menu()
        
    # Method to define the Main menu
    def menu(self):
        user_input = input("""Welcome to chatbook!! How would you like to proceed?
                           1. Press 1 to signup
                           2. Press 2 to signin
                           3. Press 3 to write a post
                           4. Press 4 to message a friend
                           5. Press any other key to exit""")
        
        if user_input == '1':
            self.signup()
        elif user_input == '2':
            self.signin()
        elif user_input == '3':
            pass
        elif user_input == '4':
            pass
        else:
            exit()
            
    def signup(self):
        email = input("Enter your email:")
        password = input("Set your password:")
        self.username = email
        self.password = password
        print("You have signed up successfully")
        print("\n")
        self.menu()        
        
    def signin(self):
        if self.username == '' and self.password == '':
            print("Please, signup first by pressing 1")
        else:
            uname = input("Enter your email/username:")
            pwd = input("Enter your password:")
            if self.username==uname and self.password==pwd:
                print("You have signed in successfully")
                self.loggedin=True
            else:
                print("Please, input correct credentials")       
                
        print("\n")
        self.menu()
        
        
         
obj = chatbook()