import json
import os
import random
import time

def entry():
    config = Config();
    activeUser = None;
    while True:
        if activeUser:
            for user in config.users:
                if user["username"] == activeUser:
                    name = user["name"];
            print(f"\nWelcome {name}, choose an activity:")
        else:
            print("Welcome to VelzBank International, choose an activity:")
        _input = input(
            "1) Register\n2) Login\n3) Send\n4) Give\n5) List\n6) Balance\n7) Logout\nPlease enter command number: ");
        if _input.isdigit():
            command = int(_input);
            if command == 1:
                activeUser = register(config);
            elif command == 2:
                activeUser = login(config);
            elif command == 3:
                if activeUser:
                    send(config, activeUser);
                else:
                    print("Please login to use this command");
            elif command == 4:
                if activeUser:
                    for user in config.users:
                        if user["username"] == activeUser:
                            if user["isAdmin"] == True:
                                give(config);
                            else:
                                print("Admin only command !");
                else:
                    print("Please login to use this command");
            elif command == 5:
                list(config);
            elif command == 6:
                if activeUser:
                    balance(config, activeUser);
                else:
                    print("Please login to use this command");
            elif command == 7:
                if activeUser:
                    activeUser = None;
                    print("Logged out")
                    time.sleep(2);
                else:
                    print("Please login to use this command");
            else:
                print("Not implemented");
        else:
            print("Invalid input, try again");

def list (config):
    print(f"Number of registered users: {len(config.users)}\nDetails:");
    i = 1;
    for user in config.users:
        print(f"{i}) Name: {user['name']}, Acount ID: {user['accountNumber']}");
        i += 1;
def login(config):
    username = input("Username: ")
    password = input("Password: ")

    for user in config.users:
        if username == user["username"] and password == user["password"]:
            return user["username"]

    print("Invalid username or password")
    time.sleep(10)
    return None
def send(config, activeUser):
    transfer_made = False;
    while transfer_made == False:
        recipient_input = input("Please enter recipient Account Number: ")
        try:
            recipient = int(recipient_input)
        except ValueError:
            print("Invalid account number")
            continue

        recipient_found = False
        for user in config.users:
            if recipient == user["accountNumber"]:
                _recipient = user["username"]
                print("Recipient found!")
                recipient_found = True
                amount = input("Please insert transfer amount: ")
                if amount.isdigit():
                    _amount = int(amount)
                    for user in config.users:
                        if user["username"] == activeUser:
                            if user["balance"] < _amount:
                                print("Insufficient balance")
                                time.sleep(10)
                                break
                            else:
                                config.edit_user_balance(_recipient, False, _amount)
                                config.edit_user_balance(activeUser, True, _amount)
                                transfer_made=True
                else:
                    print("Invalid amount, try again")
            if recipient_found:
                break
        else:
            print("Recipient not found, try again")
def balance(config, activeUser):
    for user in config.users:
        if user["username"] == activeUser:
            print(f"Balance: {user['balance']}");
def give (config):
    while True:
        userFound = False;
        _username = input("Please input recipient username: ");
        for user in config.users:
            if user["username"] == _username:
                userFound = True;
                _amount = input("Please insert transfer amount: ");
                if _amount.isdigit():
                    _amount = int(_amount)
                    config.edit_user_balance(_username, False, _amount);
                    break;
                else:
                    print("Invalid amount, try again");
            else:
                print("Username not found, try again");
        if userFound:
            break;
def register(config):
    name = input("Please enter your name: ");
    username = prompt_username(config);
    email = prompt_email(config)
    password = prompt_password();
    person = Person(name, username, email, password, False);
    config.add_user(person);
    return person.username;
def prompt_username(config):
    username = input("Please enter your username: ");
    if username == "None":
        print("Reserved username");
        return prompt_username(config);
    for user in config.users:
        if username == user['username']:
            print("Username already taken");
            return prompt_username(config);
        else:
            return username;
    else:
        return username;
def prompt_email(config):
    email = input("Please enter your email address: ");
    for user in config.users:
        if email == user['email']:
            print("Email already taken");
            return prompt_email(config);
    if "@" in email:
        return email;
    else:
        print("Invalid email");
        return prompt_email();
def prompt_password():
    password = input("Please enter your password: ");
    password_confirm = input("Confirm your password: ");
    if password != password_confirm:
        print("Passwords do not match");
        return prompt_password()
    else:
        return password;

class Person:
    def __init__(self, name: str, username: str, email: str, password: str, isAdmin: bool,):
        self.name = name;
        self.username = username;
        self.email = email;
        self.password = password;
        self.balance = 0;
        self.isAdmin = isAdmin;
        self.accountNumber = random.randrange(100000000000,999999999999)
class Config:
    def __init__(self, filename="config.json"):
        self.filename = filename;
        self.users = [];

        if os.path.exists(self.filename):
            with open(filename, "r") as file:
                try:
                    self.users = json.load(file);
                except json.decoder.JSONDecodeError:
                    self.users = [];
    def add_user(self, person):
        user = {"name": person.name, "username": person.username, "email": person.email, "password": person.password,"balance": person.balance,"isAdmin": person.isAdmin, "accountNumber": person.accountNumber};
        self.users.append(user);
        self.save();
    def edit_user_balance(self, username, remove: bool, amount: int):
        if remove:
            for user in self.users:
                if user["username"] == username:
                    user["balance"] = user["balance"] - amount;
        else:
            for user in self.users:
                if user["username"] == username:
                    user["balance"] = user["balance"] + amount;
        self.save()

    def save(self):
        with open(self.filename, "w") as file:
            json.dump(self.users, file);

entry()
