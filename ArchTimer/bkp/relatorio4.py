import os
import sys
import webbrowser
import view.rel_funcs as rel


# INICIO
print()
clientPath = sys.argv[1]
clientName = sys.argv[2]
csvList = rel.getFiles(clientPath)
# print(csvList)

somaGeralTotal = 0
insertHTML = ""
userList = []

print("-------------------------------")
print("RELATORIO GERAL ESCRITÓRIO!")
print("-------------------------------")

catFile = rel.catCSV(csvList)
resultList = rel.relArquivos(catFile)
somaGeralTotal += round(resultList[2]/60, 2)

insertHTML += rel.updateInsert(resultList)

# REPLACES MARKER IN HTML WITH strHTML AND somaGeralTotal
rel.updateHTML(clientPath, insertHTML, "RELATORIO GERAL",
               clientName, somaGeralTotal)

webbrowser.open(
    'file://' + os.path.realpath(clientPath + "/logs/relatorio.html"))

print("-------------------------------")
print("TEMPO TOTAL ESCRITÓRIO= %s horas." % str(somaGeralTotal))
print("-------------------------------")
