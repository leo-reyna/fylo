import os
from termcolor import colored, cprint

# Changing directory to the desired location
os.chdir("d:/yourfolder/fylo/")

while True:
    os.system("cls")
    
    cprint("-------------------------------", "magenta")
    cprint("Sample File Reading and Writing", "magenta")
    cprint("-------------------------------", "magenta")
    
    question = "What would you like to do? "
    message = f"Hello! {question}"
    cprint(message, "blue")

    seleccion = input("Enter \"a\" to add text • \"r\" to read file • \"c\" to clear the file • \"e\" to exit: ") 

    if seleccion == "a":
        newline = input("Enter the word you would like to add: ")
        newlinewithbrk = f"\n{newline}"
        with open("samplefile.txt", "a") as file:
            file.write(newlinewithbrk)
            cprint("Added text!", "magenta")
            input("Press any key to continue")           

    elif seleccion == "r":
        print("Reading the file...")
        with open("samplefile.txt", "r") as file:
            print(file.read())
        input("Press enter to continue...")

    elif seleccion == "e":
        print("Exiting now...")
        break

    elif seleccion == "c":
        clearselection = input("Are you sure you want to clear the contents of the file? (This cannot be undone) (y/n): ")
        if clearselection == "y":
            with open("samplefile.txt", "w") as file:
                file.write("")
                input("Press any key to continue...")
                print("File contents were cleared!")
                 
        elif clearselection == "n":
            print("Exiting now...")
        
    else:
        print("Invalid input. Enter \"a\" to add a line • \"r\" to read file • \"c\" to clear the file • \"e\" to exit")
        input("Press enter to continue...")
