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
            pass
        if user_input == "2":
            pass
        if user_input == "3":
            pass
        if user_input == "4":
            pass
        else:
            exit()


obj = chatbook()