from tkinter import Tk
from tkinter.filedialog import askdirectory

def guiClientPath(t3, END="", dir1="C:\\"):
    root = Tk()
    ftypes = [('htm file',"*.htm")]
    ttl  = "Selecione o diretório do cliente"
    root.path = askdirectory(initialdir = dir1, title = ttl)
    if END!="":
        t3.delete('1.0', END)
    t3.insert('1.0', root.path + "/")
    root.destroy()