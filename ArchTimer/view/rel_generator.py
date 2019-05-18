import os
# import sys
import webbrowser
import view.rel_funcs as rel

print()
somaGeralTotal = 0
insertHTML = ""
monthList = []
userList = []


def relatorio1(clientPath, clientName):
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

    return somaGeralTotal


def relatorio2(clientPath, clientName):
    somaGeralTotal = 0
    insertHTML = ""
    monthList = []

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

    return somaGeralTotal


def relatorio3(clientPath, clientName):
    print("-------------------------------")
    print("RELATORIO GERAL ESCRITÓRIO!")
    print("-------------------------------")

    somaGeralTotal = 0
    insertHTML = ""
    userList = []

    csvList = rel.getFiles(clientPath)

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
        'file://' + os.path.realpath(clientPath + "/logs/relatorio.html"))

    print("-------------------------------")
    print("TEMPO TOTAL ESCRITÓRIO= %s horas." % str(somaGeralTotal))
    print("-------------------------------")
    return somaGeralTotal


def relatorio4(clientPath, clientName):
    print("-------------------------------")
    print("RELATORIO GERAL ESCRITÓRIO!")
    print("-------------------------------")

    somaGeralTotal = 0
    insertHTML = ""

    csvList = rel.getFiles(clientPath)
    catFile = rel.catCSV(csvList)
    resultList = rel.relArquivos(catFile)
    somaGeralTotal += round(resultList[2]/60, 2)
    insertHTML += rel.updateInsert(resultList)

    # REPLACES MARKER IN HTML WITH strHTML AND somaGeralTotal
    rel.updateHTML(clientPath, insertHTML, "RELATORIO GERAL",
                   clientName, somaGeralTotal)
    # OPENS BROWSER
    webbrowser.open(
        'file://' + os.path.realpath(clientPath + "/logs/relatorio.html"))

    print("-------------------------------")
    print("TEMPO TOTAL ESCRITÓRIO= %s horas." % str(somaGeralTotal))
    print("-------------------------------")
    return somaGeralTotal

# relatorio1("/home/vinicius/Dropbox/logs", "SM_Cristal")
