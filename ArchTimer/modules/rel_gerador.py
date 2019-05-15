import pandas
import os

templatePath = "template/template_html.html"
templateTable = """<div class="title user" style="text-align: center" >{userName}
</div><div id="tabela"><ul class="lista"><li class="item" style="background-color: rgb(199, 199, 199); font-weight: bold">Arquivos</li>{listFiles}</ul>
<ul class="lista"><li class="valor" style="background-color: rgb(199, 199, 199);
font-weight: bold">Tempo</li>{listTime}</ul></div>"""


def relArquivos(df):
    # global somaLocal
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
        print(file + " - "+str(round(soma/60, 2)).replace('.', ',')+" horas.")

        strFiles += "<li class='item'>%s</li>" % str(file)
        strTime += "<li class='valor'>%s horas</li>" % (
            str(round(soma/60, 2)).replace('.', ','))

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


def catCSV(csvList):
    fileList = []
    for file in csvList:
        # reg=file.split("/")[len(file.split("/"))-1].split("-")[0]
        df = pandas.read_csv(file, ";", index_col=None)
        fileList.append(df)
    catFile = pandas.concat(fileList, ignore_index=True)
    return catFile


def updateHTML(clientPath, insertHTML, clientName, somaGeralTotal):
    somaGeralTotal = str(somaGeralTotal).replace('.', ',')
    with open(templatePath, "r") as template:
        with open(clientPath + "/logs/relatorio4.html", "wt") as html:
            for line in template:
                line = line.replace('{content}', insertHTML)
                line = line.replace('{somaGeralTotal}', somaGeralTotal)
                line = line.replace('{clientName}', clientName)
                html.write(line)


def updateInsert(strHTML, user=None):
    global templateTable
    newInsert = templateTable
    newInsert = newInsert.replace('{listTime}', strHTML[1])
    newInsert = newInsert.replace('{listFiles}', strHTML[0])
    if user is None:
        newInsert = newInsert.replace(
            '{userName}', "Uso de todos os usuários:")
    else:
        newInsert = newInsert.replace('{userName}', "Usuário: "+user)
    return newInsert
