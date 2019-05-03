import os
from classes import cliente, appWorking
from guiAlert import alertUI


def checkClientList():
    with open("cfg/clientList.txt") as file:
        if (file.readline() != ""):
            pass
        else:
            alertUI("Lista de clientes não configurada!\nConfigure antes de usar!")
            quit()


def searchFiles(cliente):
    ext = [".rvt", ".dwg", ".skp", ".xls", ".doc", ".ppt"]
    fileList = []
    for root, dirs, files in os.walk(cliente.path):
        for file in files:
            for items in ext:
                if file.endswith(items):
                    fileList.append(os.path.join(
                        root, file).replace(cliente.path, ""))
    print("Arquivos localizados: " + str(fileList))
    return fileList


def fileChecker(appWorking, cliente):
    if (os.path.exists(cliente.path + appWorking.fileName)):
        try:
            file = open(cliente.path + appWorking.fileName, mode="r+")
            file.close()
        except IOError:
            print(cliente.path + appWorking.fileName.strip() + " - Arquivo em USO")
            return True
    else:
        print(cliente.path + appWorking.fileName.strip() + " - Arquivo NÃO existe")


def getConfigSets():
    cfgSets = []
    with open("cfg/config.txt") as file:
        for line in file:
            cfgSets.append(line.strip())
    return cfgSets
