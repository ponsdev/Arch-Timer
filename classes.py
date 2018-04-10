class cliente(object):

    def __init__(self, name, cod, path):
        self.name = name
        self.cod = cod
        self.path = path


def getClient(fileName):
    clientList = "clientList.txt"
    client = None
    with open(clientList, 'r') as file:
        for line in file:
            if line.split(";")[1] == fileName.split("_")[0]:
                client = cliente(line.split(";")[0], line.split(";")[
                                 1], line.split(";")[2])
            else:
                pass
    return client


def addClient(nome, cod, path):
    clientList = "clientList.txt"
    oldClient = False
    with open(clientList, 'r+') as file:
        for line in file:
            if line.split(";")[1] == cod:
                oldClient = True
        if oldClient == False:
            file.write(nome + ";" + cod + ";" + path)
    file.close()


class user(object):

    def __init__(self, name):
        self.name = name


class appWorking(object):

    def __init__(self, app, fileName):
        self.app = app
        self.fileName = fileName
