from classes import user, appWorking, getClient
from logfncs import saveLog
from winfcns import get_fg_win, get_idle_duration

user = user("vinicius")


def scriptUp():

    step = 2

    if (get_idle_duration() <= 300):
        title = get_fg_win().split(" - ")
        for i in title:
            if i.find(".rvt") != -1:
                fileName = i.replace("]", "").replace("[", "")
                cliente = getClient(fileName)
                if (cliente != None):
                    app = appWorking("revit", fileName)
                    saveLog(app, cliente, user, step)
                    break
            if i.find(".dwg") != -1:
                fileName = i.replace("]", "").replace("[", "")
                cliente = getClient(fileName)
                if (cliente != None):
                    app = appWorking("autocad", fileName)
                    saveLog(app, cliente, user, step)
                    break
            if i.find(".skp") != -1:
                fileName = i
                cliente = getClient(fileName)
                if (cliente != None):
                    app = appWorking("sketchup", fileName)
                    saveLog(app, cliente, user, step)
                    break
            if (i.find(".doc") != -1 or i.find(".docx") != -1):
                fileName = i
                cliente = getClient(fileName)
                if (cliente != None):
                    app = appWorking("word", fileName)
                    saveLog(app, cliente, user, step)
                    break
            if (i.find(".xls") != -1 or i.find(".xlsx") != -1):
                fileName = i
                cliente = getClient(fileName)
                if (cliente != None):
                    app = appWorking("excel", fileName)
                    saveLog(app, cliente, user, step)
                    break
            if (i.find(".ppt") != -1 or i.find(".pptx") != -1):
                fileName = i
                cliente = getClient(fileName)
                if (cliente != None):
                    app = appWorking("ppt", fileName)
                    saveLog(app, cliente, user, step)
                    break

    # fileList = searchFiles(cliente)
    # for file in fileList:
    #     if fileChecker(file, cliente):
    #         openedFiles.append(file)
    # print("Arquivos em USO: " + str(openedFiles))
    # saveLog(openedFiles, cliente)

    else:
        pass

    # time.sleep(step)
    # chkDupLog(cliente)
