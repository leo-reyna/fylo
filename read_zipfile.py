import zipfile

def LeerCarpetaZip(file_path):
    with zipfile.ZipFile(file_path, 'r') as ZipReferencia:
        # Print the list of files in the zip file
        print("Archivos en este carpeta Zip:")
        for file_info in ZipReferencia.infolist():
            print(file_info.filename)
        
        # Extract and print the contents of a specific file
        ArchivoEspecifico = input("Introduzca el nombre del archivo para leer el contenido: ")
        if ArchivoEspecifico in ZipReferencia.namelist():
            with ZipReferencia.open(ArchivoEspecifico) as file:
                print(f"\nMostrando el contenido de: '{ArchivoEspecifico}':")
                print(file.read().decode())
        else:
            print("Este archivo no se encuentra en la carpeta Zip.")

ZipFilePath = "ArchivoEjemplo.zip" #Cambia el path.
LeerCarpetaZip(ZipFilePath)