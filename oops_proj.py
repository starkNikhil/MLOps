class chatbook:

    __user_id = 0
    def __init__(self):
          # static variable
        self.__name = "Default user"  #hidden attribute
        self.id = chatbook.__user_id
        chatbook.__user_id+= 1
        self.userName =""
        self.password = ""
        self.loggedIn = False
        # self.menu()
    
    def get_name(self):    # getter method
        return self.__name
    
    def set_name(self,name):   # setter method
        self.__name = name
    @staticmethod
    def get_id():
        return chatbook.__user_id
    @staticmethod
    def set_id( id):
        return chatbook.__user_id = id


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
            self.my_post()
        if user_input == "4":
            self.send_message()
        else:
            exit()

    def sign_up(self):
        username = input("Enter your email -> ")
        password = input("Enter your password here -> ")
        self.userName = username
        self.password = password
        print("Sign Up successfull !!")
        print("\n")
        self.menu()
    
    def sign_in(self):
        if self.userName == '' and self.password == '':
            print("Please sign up first by pressing 1 in the main menu")
            self.menu()
        else:
            username = input("Enter your username -> ")
            psd = input("Enter your password -> ")
            if username == self.userName and psd == self.password:
                print("Sign In successfull !!")
                self.loggedIn = True
                # self.menu()
            else:
                print("Invalid username or password")
        print("\n")
        self.menu()

    def my_post(self):
        if self.loggedIn== True:
            text = input("Emter your message here: ")
            print(f"Following content has been postext -> {text}")
        else:
            print("You need to sign in First to post someting...")
        
        print("\n")
        self.menu()

    def send_message(self):
        if self.loggedIn == True:
            txt = input("Enter your message here -> ")
            friend = input("Enter your firend's user name here ->")
            print(f"Your message has been sent to -> {friend}")
        else:
            print("You need to sign in First to post someting...")
        
        print("\n")
        self.menu()


# obj = chatbook()