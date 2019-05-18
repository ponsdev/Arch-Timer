import os
import sys
import webbrowser
import view.rel_funcs as rel


# INICIO
print()
clientPath = sys.argv[1]
clientName = sys.argv[2]
somaGeralTotal = 0
insertHTML = ""
monthList = []
userList = []

csvList = rel.getFiles(clientPath)

for file in csvList:
    reg = file.split("/")[len(file.split("/"))-1]
    user = reg.split("-")[0]
    month = reg.split("-")[3].replace(".csv", "")
    if month in monthList:
        break
    else:
        monthList.append(int(month))

monthList = sorted(set(monthList))
print(monthList)
for month in monthList:
    print("-------------------------------")
    print("RELATORIO MÊS %s POR ARQUIVOS!" % month)
    print("-------------------------------")
    catFile = rel.catCSV(csvList, None, month)
    resultList = rel.relArquivos(catFile, None, month)
    somaGeralTotal += round(resultList[2]/60, 2)

    insertHTML += rel.updateInsert(resultList, None, month)

print("-------------------------------")
print("TEMPO TOTAL ESCRITÓRIO= %s minutos." % str(somaGeralTotal))
print("-------------------------------")

# REPLACES MARKER IN HTML WITH strHTML AND somaGeralTotal
rel.updateHTML(clientPath, insertHTML,
               "RELATORIO MENSAL ESCRITÓRIO", clientName, somaGeralTotal)

webbrowser.open(
    'file://' + os.path.realpath(clientPath + "/logs/relatorio.html"))
