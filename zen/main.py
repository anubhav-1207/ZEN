import startup
from startup.startupfile import initialise

print("Welcome To Zen")


def usernameAuthentication():
    try:
        with open("authentication/data/username.zenlog", 'r') as milk:
            username = milk.read()
            print(f"Welcome {username},")
                
    except FileNotFoundError:
        username = input("Set Username: ")

        if username == " ":
            print("Empty Space")
            


        else:
            with open("authentication/data/username.zenlog", 'w') as milk:
                milk.write(username)

def passwordAuthentication():
    count = 0
    
    try:
        with open("authentication/data/password.zenlog",'r') as milk:
            password = milk.read()

            count = 0

            while count != 5:
                userPasswordInput = input("Password: ")
                count += 1
                
                if password != userPasswordInput:
                    print("Wrong Password")
                    continue

                else:
                    initialise()

            print("Maximum Number Of Tried Exceeded!")

            
    except FileNotFoundError:
        password = input("Set a new pasword: ")

        with open("authentication/data/password.zenlog",'w') as milk:
            milk.write(password)

usernameAuthentication()
passwordAuthentication()