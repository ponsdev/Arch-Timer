import os
import sys
import webbrowser
import modules.rel_gerador as rel


# INICIO
print()
clientPath = sys.argv[1]
clientName = sys.argv[2]
csvList = rel.getFiles(clientPath)

somaGeralTotal = 0
insertHTML = ""
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

    catFile = rel.catCSV(csvList, user)
    resultList = rel.relArquivos(catFile, user)
    somaGeralTotal += round(resultList[2]/60, 2)

    insertHTML += rel.updateInsert(resultList, user)

# REPLACES MARKER IN HTML WITH strHTML AND somaGeralTotal
rel.updateHTML(clientPath, insertHTML, "RELATORIO POR USUÁRIO",
               clientName, somaGeralTotal)

webbrowser.open(
    'file://' + os.path.realpath(clientPath + "/logs/relatorio4.html"))
