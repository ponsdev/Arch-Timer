import time
from scripts.script import scriptUp
from scripts.counter import check
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
    cfgSets = getConfigSets()
    userObj = user(cfgSets[0])
    CHECKER = check(userObj)

    run = True
    while run:
        time.sleep(int(cfgSets[1]))
        scriptUp(cfgSets, userObj, CHECKER)


if __name__ == '__main__':
    main()
