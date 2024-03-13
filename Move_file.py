import os, shutil

origin = "C:/Users/User/Downloads"
destiny = "C:/Users/User/Downloads/Arquivos_Documentos"

list_file = os.listdir(origin)

for file_name in list_file:
    name, extation = os.path.splitext(file_name)

    if extation == "":
        continue
    if extation in [".txt",".doc",".docx",".pdf"]:
        path1 = origin + "/" + file_name
        path2 = destiny
        path3 = path2 + "/" + file_name

        if os.path.exists(path2):
            print("Movendo ",file_name,"...")
            shutil.move(path1,path3)
        else:
            os.makedirs(path2)
            print("Movendo ",file_name,"...")
            shutil.move(path1,path3)

