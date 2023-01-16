import os
os.system("cls")

print("Sample File Reading and Writing")
print("-------------------------------")

question = "Would you like to add a line of text to the sample file (yes to add, no to read the file)? "
message = f"Hello! {question}"
print(message)
seleccion = input("y/n? ")

if seleccion == "y":
    newline = input("Enter the word you would like to add: ")
    newlinewithbrk = f"\n {newline}"
    with open("/python-othercode/fylo/samplefile.txt", "a") as file:
        file.write(newlinewithbrk)
        print("Added text!")

else:
    print("Reading the file...")
    fp = open('/python-othercode/fylo/samplefile.txt', 'r')
    print(fp.read())