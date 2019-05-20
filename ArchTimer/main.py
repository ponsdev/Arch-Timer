import time
from scripts.script import scriptUp
from models.filesfncs import checkClientList, getConfigSets
from models.classes import user
from views.guiAlert import alertUI


def main():
    print("--------------------------")
    print("Arch-Timer 1.0 iniciado...")
    print("--------------------------")
    if checkClientList() is not True:
        alertUI("Lista de clientes não configurada!\nConfigure antes de usar!")
        quit()
    run = True
    while run:
        cfgSets = getConfigSets()
        userObj = user(cfgSets[0])
        scriptUp(cfgSets, userObj)
        time.sleep(int(cfgSets[1]))


if __name__ == '__main__':
    main()
