import sys

def initialise():
    while True:
        command = input("~$ : ").strip().split()
        commandName = command[0]

        if commandName == "exit":
            sys.exit()
        
        
        