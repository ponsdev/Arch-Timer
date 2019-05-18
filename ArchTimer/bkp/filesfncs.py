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
