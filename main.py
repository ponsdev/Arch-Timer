import time
from script import scriptUp
from filesfncs import checkClientList, getConfigSets
from classes import user


def main():
    print("--------------------------")
    print("Arch-Timer 1.0 iniciado...")
    print("--------------------------")
    checkClientList()
    run = True
    while run:
        cfgSets = getConfigSets()
        userObj = user(cfgSets[0])
        scriptUp(cfgSets, userObj)
        time.sleep(int(cfgSets[1]))


if __name__ == '__main__':
    main()
