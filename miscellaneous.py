import os


class AccountManager:
    """
    This is a Class for Account Managing.
    Functions:
        encrypt_password(password): (Private) Encrypts a password using a secret key.
        register(): Prompts user for creating account info and stores it in 'users' dict and 'accounts.txt' file.
        load_users(): Loads user account information from the 'accounts.txt' file into the 'users' dict.
        login(): Prompts the user to login and checks if it matches a stored user account in the 'user' dict.
    """

    def __init__(self):
        self.users = {}
        if os.path.exists("accounts.txt"):
            self.load_users()

    def __encrypt_password(self, password):  # (Private) Encrypts a password using a secret key.

        __secret_key = "MathintheModernWorld"
        encrypted_password = ""
        for i, char in enumerate(password):  # Shifts each characters by certain amount depending on the '__secret_key'
            shift = ord(__secret_key[i % len(__secret_key)]) - ord('a')
            shifted_char = chr((ord(char) - ord('a') + shift) % 26 + ord('a'))
            encrypted_password += shifted_char
        return encrypted_password

    def register(self):  # Prompts user for creating account info and stores it in 'users' dict and 'accounts.txt' file.

        while True:
            username = input("Enter your username: ")
            if username in self.users:
                print("Username already exists. Please choose a different username.")
            else:
                break
        password = input("Enter a password: ")
        encrypted_password = self.__encrypt_password(password)
        self.users[username] = {'password': encrypted_password}
        with open("accounts.txt", 'a') as file:  # Appends every account into 'accounts.txt'
            file.write(f"{username}:{encrypted_password}\n")
        print("Registration successful.")
        return username

    def load_users(self):  # Loads user account information from the 'accounts.txt' file into the 'users' dict.
        with open("accounts.txt", 'r') as file:
            for line in file:
                username, encrypted_password = line.strip().split(':')
                self.users[username] = {'password': encrypted_password}

    def login(self):  # Prompts the user to login and checks if it matches a stored user account in the 'user' dict.
        username = input("Enter your username: ")
        password = input("Enter your password: ")
        encrypted_password = self.__encrypt_password(password)
        if username in self.users and self.users[username]['password'] == encrypted_password:
            print(f"Welcome, {username}!")
        else:
            print("Invalid username or password.")
        return username


class ErrorHandler:
    @staticmethod
    def get_valid_option(prompt, valid_options):
        while True:
            option = input(prompt)
            if option in valid_options:
                return option
            else:
                print(f"Invalid input.")

    @staticmethod
    def get_float(prompt):
        while True:
            try:
                return float(input(prompt))
            except ValueError:
                print("Invalid input. Please enter a valid float value.")

    @staticmethod
    def get_int(prompt):
        while True:
            try:
                return int(input(prompt))
            except ValueError:
                print("Invalid input. Please enter a valid integer value.")



