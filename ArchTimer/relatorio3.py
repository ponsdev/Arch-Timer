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
    # print("\n")
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
clientPath = sys.argv[1]
csvList = getCSV(clientPath)
print(csvList)
somaGeralTotal = 0
userList = []
for file in csvList:
    reg = file.split("/")[len(file.split("/"))-1]
    user = reg.split("-")[0]
    month = reg.split("-")[3].replace(".csv", "")
    userList.append(user)
userList = list(set(userList))
print(userList)

for user in userList:
    print("RELATORIO GERAL %s!" % user)
    catFile = catCSV(csvList, user)
    somaTotal = relArquivos(catFile, user)
    somaGeralTotal += somaTotal

# print("-------------------------------")
# print("TEMPO TOTAL ESCRITÓRIO= %s minutos." % str(somaGeralTotal))
# print("-------------------------------")
