import os
import sys
import webbrowser
import view.rel_funcs as rel


# INICIO
print()
clientPath = sys.argv[1]
clientName = sys.argv[2]
csvList = rel.getFiles(clientPath)

somaGeralTotal = 0
insertHTML = ""
monthList = []
userList = []

for file in csvList:
    reg = file.split("/")[len(file.split("/"))-1]
    user = reg.split("-")[0]
    month = reg.split("-")[3].replace(".csv", "")

    userList.append(user)
    monthList.append(int(month))

monthList, userList = zip(*sorted(zip(monthList, userList)))

n = 0
while (n < len(monthList)):
    catFile = rel.catCSV(csvList, userList[n], monthList[n])
    resultList = rel.relArquivos(catFile, userList[n], monthList[n])
    somaGeralTotal += round(resultList[2]/60, 2)

    insertHTML += rel.updateInsert(resultList, userList[n], monthList[n])
    n += 1

print("-------------------------------")
print("TEMPO TOTAL ESCRITÓRIO= %s minutos." % str(somaGeralTotal))
print("-------------------------------")

# REPLACES MARKER IN HTML WITH strHTML AND somaGeralTotal
rel.updateHTML(clientPath, insertHTML,
               "RELATORIO MENSAL POR USUÁRIO", clientName, somaGeralTotal)

webbrowser.open(
    'file://' + os.path.realpath(clientPath + "/logs/relatorio.html"))
