import os
from filesFcns import searchFiles, renameFile, removeSpaces
from guiAlert import alertUI
from guiDirPath import guiClientPath


def main():
    print("--------------------------")
    print("Renomeador pastas.........")
    print("--------------------------")
    print("\n")
    clientePath = guiClientPath()
    print(clientePath)
    print("Digite o código do cliente (Ex.: 18001_EP_P01.dwg):")
    clienteCod = input()
    option = ""
    while not option in ("s", "n"):
        print("Deseja alterar as pastas internas? (S/N)")
        option = input().lower()
        print(option)

    fileList = searchFiles(clientePath)
    print(fileList)
    for file in fileList:
        removeSpaces(file, clientePath, clienteCod)
        pass

    fileList = searchFiles(clientePath)
    print(fileList)
    for file in fileList:
        renameFile(file, clientePath, clienteCod, option)
        pass
    alertUI("Arquivos renomeados!!!")
    input()


main()
