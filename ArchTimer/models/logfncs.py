import os.path
import datetime
import time


def saveLog(appRunning, cliente, user, cfgSets):
    step = int(cfgSets[1])
    today = datetime.date.today()
    arqLog = "logs/"+user.name+"-timeLog-mes-" + str(today.month) + ".csv"
    try:
        file = open(cliente.path.strip() + arqLog, mode="r+")
    except IOError:
        file = open(cliente.path.strip() + arqLog, mode="w")

    newFile = True
    try:
        content = file.readlines()
        file.seek(0)

        for line in content:
            if (line.split(";")[1] != str(today.day)):
                file.write(line)
            else:
                if (appRunning.fileName != line.split(";")[2]):
                    file.write(line)
                else:
                    tempo = float(line.split(";")[3]) + step/60
                    file.write(user.name + ";" + str(today.day) +
                               ";" + appRunning.fileName + ";" + str(tempo) + "\n")
                    newFile = False
    except:
        print('arquivo log criado')
        file.write("usuario;dia;arquivo;tempo\n")

    if (newFile == True):
        file.write(user.name + ";" + str(today.day) +
                   ";" + appRunning.fileName + ";" + str(step/60) + "\n")

    file.truncate()
    print(appRunning.fileName + " - Logged... - " +
          time.strftime("%H:%M:%S, %d/%m/%Y", time.localtime()))
    file.close()


def logPathChecker(path):
    if os.path.isdir(path+"logs/"):
        pass
    else:
        os.makedirs(path+"logs/")
        print("Pasta de logs criada!")
    return 0


# logPathChecker("fsdfad")
