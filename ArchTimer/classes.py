import os
from guiAlert import alertUI
from models.logfncs import logPathChecker

clientList = "cfg/clientList.txt"
configList = "cfg/config.txt"


class cliente(object):

    def __init__(self, name, cod, path):
        self.name = name
        self.cod = cod
        self.path = path


def getClient(fileName):
    client = None
    with open(clientList, 'r') as file:
        for line in file:
            # if line.split(";")[1] == fileName.split("_")[0]:
            #     client = cliente(line.split(";")[0], line.split(";")[
            #                      1], line.split(";")[2])
            if fileName.find(line.split(";")[1]) != -1:
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


def addClient(win, name, cod, path, id, lbIn):
    if (name == "" or cod == "" or path == ""):
        alertUI("Ha um campo vazio!")
    else:
        oldClient = False
        with open(clientList, 'r+') as file:
            content = file.readlines()
            file.seek(0)
            for line in content:
                if line.split(";")[1] == cod:
                    oldClient = True
                    file.write(line)
                    alertUI("Código já cadastrado!")
                    break
                else:
                    file.write(line)
            if oldClient is False:
                file.write(name + ";" + cod + ";" + path + "\n")
            file.truncate()
            file.close()
            lbIn.insert(id, name + " - Cod:" + cod + " - " + path.strip())
    logPathChecker(path)
    win.destroy()
    alertUI("Cliente adicionado!")


def delClient(item, lb1, END):
    lb1.delete(0, END)
    with open(clientList, 'r+') as file:
        content = file.readlines()
        file.seek(0)
        for line in content:
            clienteID = line.split(";")[1]
            if (item.split(" - ")[1].replace("Cod:", "") != clienteID):
                file.write(line)
            else:
                pass
        file.truncate()
        file.close()
    clients = readClients()
    id = 0
    for i in clients:
        id += 1
        lb1.insert(id, i.name + " - Cod:" + i.cod + " - " + i.path.strip())


def changeClient(win, name, cod, path, lbIn, END, id, item):
    if (name == "" or cod == "" or path == ""):
        alertUI("Ha um campo vazio!")
    else:
        delClient(item, lbIn, END)
        oldClient = False
        with open(clientList, 'r+') as file:
            content = file.readlines()
            file.seek(0)
            for line in content:
                if line.split(";")[1] == cod:
                    oldClient = True
                    file.write(line)
                    break
                else:
                    file.write(line)
            if oldClient is False:
                file.write(name + ";" + cod + ";" + path + "\n")
            file.truncate()
            file.close()
            lbIn.insert(id, name + " - Cod:" + cod + " - " + path.strip())
    logPathChecker(path)
    win.destroy()
    alertUI("Cliente alterado!!!")


class user(object):

    def __init__(self, name):
        self.name = name


def getUser():
    with open(configList, "r") as file:
        user = file.readlines()[0].strip()
        if user == "user_std":
            user = os.getlogin()
    return user


def setUser(win, labelUser, user, cfgSets):
    with open(configList, "r+") as file:
        content = file.readlines()
        file.seek(0)
        i = 1
        for line in content:
            if i == 1:
                file.write(user + "\n")
            else:
                file.write(line)
            i += 1
        file.truncate()
        file.close()
    win.destroy()
    labelUser.set(user)


class appWorking(object):

    def __init__(self, app, fileName):
        self.app = app
        self.fileName = fileName
