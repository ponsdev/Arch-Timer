import time
from classes import *
from logfncs import *
from filesfncs import *
from winfcns import *
from win32gui import GetWindowText, GetForegroundWindow

run = True
step = 120
#cliente = cliente("nome", "18001", "C:/TIMER/timer/")
user = user("vinicius")

while run:

    openedFiles = []

    if (get_idle_duration() <= 180):
        title = get_fg_win().split(" - ")
        for i in title:
            if i.find(".rvt") != -1:
                fileName = title[2].replace("]", "")
                cliente = getClient(fileName)
                if (cliente != None):
                    app = appWorking("revit", fileName)
                    saveLog(app, cliente, user)
                    break
            if i.find(".dwg") != -1:
                fileName = i.replace("]", "").replace("[", "")
                cliente = getClient(fileName)
                if (cliente != None):
                    app = appWorking("autocad", fileName)
                    saveLog(app, cliente, user)
                    break
            if i.find(".skp") != -1:
                fileName = i
                cliente = getClient(fileName)
                if (cliente != None):
                    app = appWorking("sketchup", fileName)
                    saveLog(app, cliente, user)
                    break

        # fileList = searchFiles(cliente)
        # for file in fileList:
        #     if fileChecker(file, cliente):
        #         openedFiles.append(file)
        # print("Arquivos em USO: " + str(openedFiles))
        # saveLog(openedFiles, cliente)
    else:
        pass

    # chkDupLog(cliente)

    time.sleep(step)
