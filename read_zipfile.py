import zipfile

def ReadZipFile(file_path):
    with zipfile.ZipFile(file_path, 'r') as ZipReferencia:
        # Print the list of files in the zip file
        print("Files in this zip file:")
        for file_info in ZipReferencia.infolist():
            print(file_info.filename)
        
        # Extract and print the contents of a specific file
        specific_file = input("Enter the name of a file to read its contents: ")
        if specific_file in ZipReferencia.namelist():
            with ZipReferencia.open(specific_file) as file:
                print(f"\nShowing contents of '{specific_file}':")
                print(file.read().decode())
        else:
            print("File not found in the zip file.")

ZipFilePath = "example.zip" #change path accordingly
ReadZipFile(ZipFilePath)