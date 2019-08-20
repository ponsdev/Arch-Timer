from models.classes import appWorking, getClient
from models.logfncs import saveLog
from models.winfcns import get_fg_win, get_idle_duration


def cleanFN(title):
    filename = title.strip()
    filename = filename.replace("[", "").replace("]", "")
    filename = filename.replace("(", "").replace(")", "")
    filename = filename.replace("Não está respondendo", "").strip()
    filename = filename.replace("Not Responding", "").strip()
    return filename


def scriptUp(cfgSets, user, CHECKER):
    if (get_idle_duration() <= 300):
        title = get_fg_win().split(" - ")
        app = None
        for i in title:
            if i.find(".rvt") != -1:
                filename = cleanFN(i)
                cliente = getClient(filename)
                if (cliente is not None):
                    app = appWorking("revit", filename, cliente)
                    # saveLog(app, cliente, user, cfgSets)
                    CHECKER(cfgSets, app)
                break
            elif i.find(".dwg") != -1:
                filename = cleanFN(i)
                cliente = getClient(filename)
                if (cliente is not None):
                    app = appWorking("autocad", filename, cliente)
                    # saveLog(app, cliente, user, cfgSets)
                    CHECKER(cfgSets, app)
                    break
            elif i.find(".skp") != -1:
                filename = cleanFN(i)
                cliente = getClient(filename)
                if (cliente is not None):
                    app = appWorking("sketchup", filename, cliente)
                    # saveLog(app, cliente, user, cfgSets)
                    CHECKER(cfgSets, app)
                    break
            elif (i.find(".doc") != -1 or i.find(".docx") != -1):
                filename = cleanFN(i)
                cliente = getClient(filename)
                if (cliente is not None):
                    app = appWorking("word", filename, cliente)
                    # saveLog(app, cliente, user, cfgSets)
                    CHECKER(cfgSets, app)
                    break
            elif (i.find(".xls") != -1 or i.find(".xlsx") != -1):
                filename = cleanFN(i)
                cliente = getClient(filename)
                if (cliente is not None):
                    app = appWorking("excel", filename, cliente)
                    # saveLog(app, cliente, user, cfgSets)
                    CHECKER(cfgSets, app)
                    break
            elif (i.find(".ppt") != -1 or i.find(".pptx") != -1):
                filename = cleanFN(i)
                cliente = getClient(filename)
                if (cliente is not None):
                    app = appWorking("ppt", filename, cliente)
                    # saveLog(app, cliente, user, cfgSets)
                    CHECKER(cfgSets, app)
                    break

        if app is None:
            app = appWorking("outro", 'none', None)
            CHECKER(cfgSets, app)

    else:
        pass
