from tkinter import Tk
from tkinter.filedialog import askdirectory


def guiClientPath():
    dir1 = "C:\\"
    ttl = "Selecione o diretório do cliente"
    root = Tk()
    root.path = askdirectory(initialdir=dir1, title=ttl)
    root.destroy()
    return root.path+"/"
