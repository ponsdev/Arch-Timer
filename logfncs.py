import os.path
import datetime
from classes import cliente, appWorking, user


def chkDupLog(cliente):
    today = datetime.date.today()
    arqLog = "timeLog-mes-" + str(today.month) + ".csv"
    try:
        file = open(cliente.path + arqLog, mode="r+")
    except IOError:
        file = open(cliente.path + arqLog, mode="w")
    content = file.readlines()
    file.seek(0)

    linesDel = []
    for line1 in content:
        bool = False
        temp = line1.split(";")[0] + ";" + \
            line1.split(";")[1] + ";" + line1.split(";")[2]
        if temp in linesDel:
            pass
        else:
            for line2 in content:
                if (line1.split(";")[0] == line2.split(";")[0] and
                    line1.split(";")[1] == line2.split(";")[1] and
                    line1.split(";")[2] == line2.split(";")[2] and
                        line1.split(";")[3] != line2.split(";")[3]):
                    linesDel.append(line1.split(";")[0] + ";" +
                                    line1.split(";")[1] + ";" + line1.split(";")[2])
                    bool = True
                    tempo = float(line1.split(
                        ";")[3]) + float(line2.split(";")[3])
                    print("atualizou")
                    pass
        if bool:
            file.write(line1.split(";")[
                0] + ";" + line1.split(";")[1] + ";" +
                line1.split(";")[2] + ";" + str(tempo) + "\n")
        else:
            if temp not in linesDel:
                print("original")
                file.write(line1)
            if temp in linesDel:
                pass
    file.truncate()
    file.close()
    print("Arquivos OK!")
    input()


def saveLog(appRunning, cliente, user, step):
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

    if (newFile == True):
        file.write(user.name + ";" + str(today.day) +
                   ";" + appRunning.fileName + ";" + step/60 + "\n")

    file.truncate()
    print(appRunning.fileName + " - Salvo!!")
    file.close()
