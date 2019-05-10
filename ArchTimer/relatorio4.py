import pandas
import os
import sys
import webbrowser

# filePath="vinicius-timeLog-mes-5.csv"
templatePath = "template/template.html"


def relArquivos(df):
    global somaTotal
    df = df.set_index("arquivo")
    filesListed = list(set(df.index))
    # somaTotal = 0
    strHTML = ""

    for file in filesListed:
        soma = 0
        if str(type(df.loc[file, "tempo"])) == "<class 'numpy.float64'>":
            soma = df.loc[file, "tempo"]
            somaTotal += soma
        if type(df.loc[file, "tempo"]) is pandas.core.series.Series:
            listaTempo = list(df.loc[file, "tempo"])
            for i in listaTempo:
                # print(i)
                soma += float(i)
            somaTotal += soma
        print(file + " - "+str(round(soma/60, 2)).replace('.', ',')+" horas.")
        strHTML += "<li class='item'>%s horas.</li>" % (
            file + " - "+str(round(soma/60, 2)).replace('.', ','))
    # print("\n")

    return strHTML


def getCSV(clientPath):
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


def updateHTML(strHTML, somaGeralTotal):
    global clientPath
    with open(templatePath, "r") as template:
        with open(clientPath + "/logs/relatorio4.html", "wt") as html:
            for line in template:
                html.write(line.replace('{listaItens}', strHTML).replace(
                    '{somaTotal}', str(somaGeralTotal).replace('.', ',')))


# INICIO
clientPath = sys.argv[1]
csvList = getCSV(clientPath)
# print(csvList)

somaGeralTotal = 0
somaTotal = 0

# for file in csvList:
#     reg=file.split("/")[len(file.split("/"))-1]
#     user=reg.split("-")[0]
#     month=reg.split("-")[3].replace(".csv","")
#     userList.append(user)
# userList=list(set(userList))
# print(userList)

print("-------------------------------")
print("RELATORIO GERAL ESCRITÓRIO!")

catFile = catCSV(csvList)
strHTML = relArquivos(catFile)
somaGeralTotal += round(somaTotal/60, 2)
updateHTML(strHTML, somaGeralTotal)

webbrowser.open(
    'file://' + os.path.realpath(clientPath + "/logs/relatorio4.html"))

print("-------------------------------")
print("TEMPO TOTAL ESCRITÓRIO= %s horas." % str(somaGeralTotal))
print("-------------------------------")
