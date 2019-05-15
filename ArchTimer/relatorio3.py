import pandas
import os
import sys

# filePath="vinicius-timeLog-mes-5.csv"


def relArquivos(df, user):
    df = df.set_index("arquivo")

    # reg=filePath.split("/")[len(filePath.split("/"))-1]
    # # reg=reg.split("\\")[len(reg.split("\\"))-1]
    # user=reg.split("-")[0]
    # month=reg.split("-")[3].replace(".csv","")

    filesListed = list(set(df.index))
    somaTotal = 0

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
        print(file + " - "+str(soma))

    print("TEMPO TOTAL GERAL %s = %s minutos." % (user, str(somaTotal)))
    print("-------------------------------")

    return somaTotal


def getCSV(clientPath):
    ext = ".csv"
    csvList = []
    for root, dirs, files in os.walk(clientPath):
        for file in files:
            if file.endswith(ext):
                csvList.append(os.path.join(root, file).replace("\\", "/"))
    return csvList


def catCSV(csvList, user):
    fileList = []
    for file in csvList:
        reg = file.split("/")[len(file.split("/"))-1].split("-")[0]
        if (str(reg) == str(user)):
            df = pandas.read_csv(file, ";", index_col=None)
            fileList.append(df)
    catFile = pandas.concat(fileList, ignore_index=True)
    return catFile


# INICIO
print()
clientPath = sys.argv[1]
clientName = sys.argv[2]
csvList = getCSV(clientPath)

somaGeralTotal = 0
somaTotal = 0
userList = []


for file in csvList:
    reg = file.split("/")[len(file.split("/"))-1]
    user = reg.split("-")[0]
    month = reg.split("-")[3].replace(".csv", "")
    userList.append(user)
userList = list(set(userList))

for user in userList:
    print("-------------------------------")
    print("RELATORIO GERAL %s!" % user)
    print("-------------------------------")

    catFile = catCSV(csvList, user)
    strHTML = relArquivos(catFile, user)

    # somaTotal = relArquivos(catFile, user)
    somaGeralTotal += round(somaTotal/60, 2)

# REPLACES MARKER IN HTML WITH strHTML AND somaGeralTotal
# updateHTML(strHTML, somaGeralTotal, clientName)

# webbrowser.open(
#     'file://' + os.path.realpath(clientPath + "/logs/relatorio4.html"))
