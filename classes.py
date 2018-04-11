clientList = "clientList.txt"


class cliente(object):

    def __init__(self, name, cod, path):
        self.name = name
        self.cod = cod
        self.path = path


def getClient(fileName):
    client = None
    with open(clientList, 'r') as file:
        for line in file:
            if line.split(";")[1] == fileName.split("_")[0]:
                client = cliente(line.split(";")[0], line.split(";")[
                                 1], line.split(";")[2])
            else:
                pass
    return client


def readClients():
    clients = []
    with open(clientList, 'r') as file:
        for line in file:
            client = cliente(line.split(";")[0], line.split(";")[
                1], line.split(";")[2])
            clients.append(client)
    return clients


def addClient(nome, cod, path):
    oldClient = False
    with open(clientList, 'r+') as file:
        for line in file:
            if line.split(";")[1] == cod:
                oldClient = True
        if oldClient == False:
            file.write(nome + ";" + cod + ";" + path)
    file.close()


def delClient(cliente, lb1):
    # lb1.delete(0, END)
    with open(clientList, 'r+') as file:
        content = file.readlines()
        file.seek(0)
        for line in content:
            print(cliente.split(" - ")[1].replace("Cod:", ""))
            print(line.split(";")[1])
            if (cliente.split(" - ")[1].replace("Cod:", "") != line.split(";")[1]):
                file.write(line)
            else:
                pass
        file.truncate()
        file.close()
        win.update()


class user(object):

    def __init__(self, name):
        self.name = name


class appWorking(object):

    def __init__(self, app, fileName):
        self.app = app
        self.fileName = fileName
