# Name: fylo.py
# Description: simple script to open an specific file locally
# by RL - Jan 2023
#https://thispointer.com/how-to-append-text-or-lines-to-a-file-in-python/#:~:text=Append%20data%20to%20a%20file%20as%20a%20new,using%20write%20%28%29%20function.%204%20Close%20the%20file

import os
os.system("clear")
os.system("cls")

question = "Would you like to add to the Sample text file?"
message = f"Hello! {question}"
print(message)
seleccion = input("y/n ")
if seleccion == "y":
    #file_object = open('/python-othercode/fylo/sample.txt', 'a') # "a" checks if the file exists
    #agregado = input("What would you like to add? ")
    #file_object.write(agregado)
    #file_object.write("hello2")
    with open("/python-othercode/fylo/sample.txt", "a") as file:
    # Write the string to the file
        file.write("This is a new line appended to the file.\n")

    with open("/python-othercode/fylo/sample.txt", "a+") as file_object:
        file_object.seek(0)
        data = file_object.read(100)
        if len(data) > 0:
            #file_object.write("/n")
            #file_object.write("agregado \n")
            print("added text!")
    #file_object.closey

elif seleccion == "n":
    print("I will read it contents then.")
    fp = open('/python-othercode/fylo/sample.txt', 'r') # opening a file on read mode
    print(fp.read())
    fp.close

