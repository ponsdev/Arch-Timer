import pandas
import os

monthName = ['Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho',
             'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro']
templatePath = "template_html.html"
templateTable = """<div class="container title user">{userName}</div><div id="tabela"><ul class="lista"><li class="item" style="background-color: rgb(230, 230, 230); font-weight: bold">Arquivos</li>{listFiles}<li class="item" style="background-color: rgb(230, 230, 230); font-weight: bold">Total</li></ul><ul class="lista"><li lass="valor" style="background-color: rgb(230, 230, 230); font-weight: bold; text-align: right">Tempo</li>{listTime}<li lass="valor" style="background-color: rgb(230, 230, 230); font-weight: bold; text-align: right">{somaLocal}</li></ul></div>"""


def relArquivos(df, user=None, month=None):
    df = df.set_index("arquivo")
    filesListed = list(set(df.index))
    somaLocal = 0
    strHTML = []
    strFiles = ""
    strTime = ""

    for file in filesListed:
        soma = 0
        if str(type(df.loc[file, "tempo"])) == "<class 'numpy.float64'>":
            soma = df.loc[file, "tempo"]
            somaLocal += soma
        if type(df.loc[file, "tempo"]) is pandas.core.series.Series:
            listaTempo = list(df.loc[file, "tempo"])
            for i in listaTempo:
                # print(i)
                soma += float(i)
            somaLocal += soma
        print(file + " - "+str(round(soma/60, 2)).replace('.', ',')+" horas")

        strFiles += "<li class='item'>%s</li>" % str(file)
        strTime += "<li class='valor'>%s horas</li>" % (
            str("{: .2f}".format(round(soma/60, 2)).replace('.', ',')))

    strHTML.append(strFiles)
    strHTML.append(strTime)
    strHTML.append(somaLocal)

    return strHTML


def getFiles(clientPath):
    ext = ".csv"
    csvList = []
    for root, dirs, files in os.walk(clientPath):
        for file in files:
            if file.endswith(ext):
                csvList.append(os.path.join(root, file).replace("\\", "/"))
    return csvList


def catCSV(csvList, user=None, month=None):
    fileList = []
    for file in csvList:
        regUser = file.split("/")[len(file.split("/"))-1].split("-")[0]
        regMonth = file.split("/")[len(file.split("/")) -
                                   1].split("-")[3].replace(".csv", "")
        if ((user is None) or (str(regUser) == str(user))):
            if (month is None) or (str(regMonth) == str(month)):
                df = pandas.read_csv(file, ";", index_col=None)
                fileList.append(df)
    catFile = pandas.concat(fileList, ignore_index=True)
    return catFile


def updateHTML(clientPath, insertHTML, relType, clientName, somaGeralTotal):
    somaGeralTotal = str("{: .2f}".format(somaGeralTotal)).replace('.', ',')
    with open(templatePath, "r") as template:
        with open(clientPath + "/logs/relatorio.html", "wt") as html:
            for line in template:
                line = line.replace('{relType}', relType)
                line = line.replace('{clientName}', clientName)
                line = line.replace('{content}', insertHTML)
                line = line.replace('{somaGeralTotal}', somaGeralTotal)
                html.write(line)


def updateInsert(resultList, user=None, month=None):
    global templateTable
    newInsert = templateTable
    newInsert = newInsert.replace('{listFiles}', resultList[0])
    newInsert = newInsert.replace('{listTime}', resultList[1])
    newInsert = newInsert.replace(
        '{somaLocal}', str("{: .2f}".format(round(resultList[2]/60, 2))).replace('.', ',')+" horas")
    if user is None and month is None:
        newInsert = newInsert.replace(
            '{userName}', "Uso de todos os usuarios:")
    if user is None and month is not None:
        newInsert = newInsert.replace(
            '{userName}', monthName[int(month)-1])
    if user is not None and month is None:
        newInsert = newInsert.replace('{userName}', "Usuario: " + user)
    if user is not None and month is not None:
        newInsert = newInsert.replace(
            '{userName}', ("Mês: %s - Usuario: %s" %
                           (monthName[int(month)-1], user)))
    return newInsert
