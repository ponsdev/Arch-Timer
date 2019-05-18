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


def getConfigSets():
    cfgSets = []
    with open("cfg/config.txt") as file:
        for line in file:
            cfgSets.append(line.strip())
    return cfgSets
