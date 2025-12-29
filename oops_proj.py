class chatbook:
    def __init__(self):
        self.userName =""
        self.password = ""
        self.loggedIn = False
        self.menu()
    
    def menu(self):
        user_input = input(""" Welcome to chatbook!! How would you like to proceed
        1. Press 1 to Sign Up
        2. Press 2 to Sign In
        3. Press 3 to write a post
        4. Press 4 to message a firend
        5. Press any other key to exit
            """)
        if user_input == "1":
            self.sign_up()
        if user_input == "2":
            self.sign_in()
        if user_input == "3":
            pass
        if user_input == "4":
            pass
        else:
            exit()

    def sign_up(self):
        email = input("Enter your email -> ")
        password = input("Enter your password here -> ")
        self.email = email
        self.password = password
        print("Sign Up successfull !!")
        print("\n")
        self.menu()
    
    def sign_in(self):
        if self.userName == '' and self.password == '':
            print("Please sign up first by pressing 1 in the main menu")
            self.menu()
        else:
            userName = input("Enter your username -> ")
            password = input("Enter your password -> ")
            if userName == self.userName and password == self.password:
                print("Sign In successfull !!")
                self.loggedIn = True
                # self.menu()
            else:
                print("Invalid username or password")
        print("\n")
        self.menu()

obj = chatbook()