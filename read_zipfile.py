import zipfile

def ReadZipFile(file_path):
    with zipfile.ZipFile(file_path, 'r') as ZipReferencia:
        # Print the list of files in the zip file
        print("Files in this zip file:")
        for file_info in ZipReferencia.infolist():
            print(file_info.filename)
        
        # Extract and print the contents of a specific file
        ArchivoEspecifico = input("Enter the name of a file to read its contents: ")
        if ArchivoEspecifico in ZipReferencia.namelist():
            with ZipReferencia.open(ArchivoEspecifico) as file:
                print(f"\nShowing contents of '{ArchivoEspecifico}':")
                print(file.read().decode())
        else:
            print("File not found in the zip file.")

ZipFilePath = "example.zip" #change path accordingly
ReadZipFile(ZipFilePath)