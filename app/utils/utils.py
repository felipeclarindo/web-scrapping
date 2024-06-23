import os

# clear terminal
def clear():
    # Verfied operacional system
    if os.name == "posix":
        os.system("clear")
    elif os.name == "nt":
        os.system("cls")
    else:
        # Simulating one clear terminal if system undefined
        print('\n'*100)