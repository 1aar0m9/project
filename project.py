from sharepoint import sharepoint

# nombre del arichivo
file_name = 'inventario.xlsmx'

# configurar el nombre de la carpeta
folder_name = 'project'

# descargar el archivo
file = sharepoint().download_file(file_name, folder_name)

# guardado
with open(file_name, 'wb') as f:
    f.write(file)
    f.close()