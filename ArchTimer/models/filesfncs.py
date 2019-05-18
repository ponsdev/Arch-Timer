# import os
# from classes import cliente, appWorking


def checkClientList():
    with open("cfg/clientList.txt") as file:
        if (file.readline() != ""):
            return True
        else:
            return False


def getConfigSets():
    cfgSets = []
    with open("cfg/config.txt") as file:
        for line in file:
            cfgSets.append(line.strip())
    return cfgSets
