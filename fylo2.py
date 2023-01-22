# RL Jan 2023
# Example of using termcolor, if statements, accessing a text file to 
# read and write, special characters, etc. 


import os
while True:
    os.system("cls")
    from termcolor import colored, cprint

    cprint("-------------------------------", "magenta")
    cprint("Sample File Reading and Writing", "magenta")
    cprint("-------------------------------", "magenta")

    question = "Would you like to do? "
    message = f"Hello! {question}"
    cprint(message, "blue")

    seleccion = input("Enter \"a\" to add test • \"r\" to read file • \"c\" to clear the file • \"e\" to Exit ") 

    if seleccion == "a":
        newline = input("Enter the word you would like to add: ")
        newlinewithbrk = f"\n {newline}"
        with open("/python-othercode/fylo/samplefile.txt", "a") as file:
            file.write(newlinewithbrk)
            cprint("Added text!", "magenta")
            input("Press any key to continue")           

    elif seleccion == "r":
        print("Reading the file...")
        fp = open('/python-othercode/fylo/samplefile.txt', 'r')
        print(fp.read())
        input("Press enter to continue...")

    elif seleccion == "e":
        print("Exiting now..")
        break

    elif seleccion =="c":
        clearselection = input("Are you sure you want to clear the contents of the file (cannot be undone) y/n ")
        if clearselection == "y":
            with open("/python-othercode/fylo/samplefile.txt", "w") as file:
                file.write("")
                input("Press any key to continue...")
                print("File contents were cleared!")
                 
        elif clearselection == "n":
            print("Exiting now..")
        
    else:
        print("Invalid input. Enter \"a\" to add a line • \"r\" to read file • \"c\" to clear the file • \"e\" to Exit")
        input("Press enter to continue...")