import pandas
import os
import sys

# filePath="vinicius-timeLog-mes-5.csv"


def relMensal(filePath):
    df = pandas.read_csv(filePath, ";", index_col=None)
    df = df.set_index("arquivo")

    reg = filePath.split("/")[len(filePath.split("/"))-1]
    reg = reg.split("\\")[len(reg.split("\\"))-1]
    user = reg.split("-")[0]
    month = reg.split("-")[3].replace(".csv", "")
    filesListed = list(set(df.index))
    somaTotal = 0
    print("-------------------------------")
    print("RELATÓRIO MÊS %s DO USUÁRIO %s:" % (month, user))
    for file in filesListed:
        soma = 0
        if str(type(df.loc[file, "tempo"])) == "<class 'numpy.float64'>":
            soma = df.loc[file, "tempo"]
            somaTotal += soma
        if type(df.loc[file, "tempo"]) is pandas.core.series.Series:
            listaTempo = list(df.loc[file, "tempo"])
            for i in listaTempo:
                soma += float(i)
            somaTotal += soma
        print(file + " - "+str(soma))
    # print("-------------------------------")
    # print("Tempo total %s= %s minutos." % (user, str(somaTotal)))
    # print("-------------------------------")

    print("USUÁRIO: %s - MÊS: %s = %s minutos." %
          (user, month, str(somaTotal)))
    return somaTotal


def getCSV(clientPath):
    ext = ".csv"
    csvList = []
    for root, dirs, files in os.walk(clientPath):
        for file in files:
            if file.endswith(ext):
                csvList.append(os.path.join(root, file))
    return csvList


clientPath = sys.argv[1]
csvList = getCSV(clientPath)
print(csvList)
somaGeralTotal = 0
for file in csvList:
    somaTotal = relMensal(file)
    somaGeralTotal += somaTotal
    # print("\n")
print("-------------------------------")
print("Tempo total escritório= %s minutos." % str(somaGeralTotal))
print("-------------------------------")
