import os
while True:
    os.system("cls")

    print("Sample File Reading and Writing")
    print("-------------------------------")

    question = "Would you like to add a line of text to the sample file (\"a\" to ADD, \"r\" to READ the file. \"e\" to EXIT)? "
    message = f"Hello! {question}"
    print(message)

    seleccion = input("Enter \"a\" or \"r\" or Type \"e\" to Exit ") 

    if seleccion == "a":
        newline = input("Enter the word you would like to add: ")
        newlinewithbrk = f"\n {newline}"
        with open("/python-othercode/fylo/samplefile.txt", "a") as file:
            file.write(newlinewithbrk)
            print("Added text!")

    elif seleccion == "r":
        print("Reading the file...")
        fp = open('/python-othercode/fylo/samplefile.txt', 'r')
        print(fp.read())
        input("Press enter to continue...")

    elif seleccion == "e":
        print("Exiting now..")
        break
        
    else:
        print("Invalid input. Please enter y or n. or e to exit")
        input("Press enter to continue...")