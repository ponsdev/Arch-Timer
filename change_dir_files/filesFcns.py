import os
from guiAlert import alertUI


def searchFiles(clientePath):
    ext = [".rvt", ".dwg", ".skp", ".xls", ".doc", ".ppt"]
    fileList = []
    for root, dirs, files in os.walk(clientePath):
        for file in files:
            for items in ext:
                if file.endswith(items):
                    fileList.append(os.path.join(
                        root, file))
    return fileList


def removeSpaces(file, clientePath, clienteCod):
    if file.find(" ") != -1:
        os.rename(file.replace("\\", "/"),
                  file.replace(" ", "_").replace("\\", "/"))
        print("Arquivo antigo: "+file +
              " - Arquivo NOVO: "+file.replace(" ", "_"))
        # alertUI("Nomes com espaços alterados!!!")


def renameFile(file, clientePath, clienteCod, option):
    print(file.find(clienteCod))
    if file.find(clienteCod) == -1:
        print(file.find("\\"))
        if file.find("\\") == -1:
            print(file)
            oldFile = file.replace(clientePath, "")
            newFile = clienteCod+"_"+oldFile
            os.rename(file, file.replace(oldFile, newFile))
        else:
            if option == "s":
                oldFile = file.split("\\")[len(file.split("\\"))-1]
                newFile = clienteCod+"_"+oldFile
                print("Arquivo antigo: "+oldFile +
                      " - Arquivo NOVO: "+newFile)
                os.rename(file.replace("\\", "/"),
                          file.replace(oldFile, newFile).replace("\\", "/").replace("-", "_"))
            else:
                pass

    else:
        # print("Arquivo já contem codigo do cliente: "+file)
        pass
