from tkinter import *
from tkinter import ttk
from classes import user, getUser, addClient, delClient, readClients
import threading
from guiChanges import changeUserUI, addClientUI, changeClientUI
from filesfncs import getConfigSets
import os

# labelUser = "usuario"


class ConfigFrame(Frame):

    def __init__(self, win, cfgSets):
        super().__init__()
        self.win = win
        self.initUI(win, cfgSets)

    def initUI(self, win, cfgSets):

        self.master.title("Arch-Timer 1.0")

        l0 = Label(win, text="Cadastro/Usuário")
        l0.grid(row=0, column=0, columnspan=4)

        labelUser = StringVar()
        l1 = Label(win, textvariable=labelUser)
        labelUser.set(getUser())
        l1.grid(row=1, column=0, columnspan=3)
        b1 = Button(win, text="Mudar usuário", width=16,
                    command=lambda: changeUserUI(labelUser, cfgSets))
        b1.grid(row=1, column=3)

        lb1 = Listbox(win, width=63, height=16, activestyle='dotbox')
        lb1.grid(row=2, column=0, rowspan=3, columnspan=3)
        # s = ttk.Scrollbar(win, orient=VERTICAL, command=lb1.yview)
        # s.grid(column=3, row=2)
        # lb1['yscrollcommand'] = s.set
        clients = readClients()
        id = 0
        for i in clients:
            id += 1
            lb1.insert(id, i.name + " - Cod:" + i.cod + " - " + i.path.strip())
        b2 = Button(win, text="Adicionar\nCliente", height=5,
                    width=16, command=lambda: (addClientUI(id+1, lb1)))
        b2.grid(row=2, column=3)
        b3 = Button(win, text="Mudar\nCliente", height=5, width=16, command=lambda: (
            changeClientUI(lb1.get(lb1.curselection()[0]), lb1, END, lb1.curselection()[0])))
        b3.grid(row=3, column=3)
        b4 = Button(win, text="Remover\nCliente", height=5,
                    width=16, command=lambda: (delClient(lb1.get(lb1.curselection()[0]), lb1, END)))
        b4.grid(row=4, column=3)

        l2 = Label(win, text="Relatórios")
        l2.grid(row=5, column=0, columnspan=4)
        b5 = Button(win, text="Mensal por\nUsuário", width=16,
                    command=(lambda: os.system("python relatorio1.py "+lb1.get(lb1.curselection()[0]).split(" - ")[2])))
        b5.grid(row=6, column=0)
        b6 = Button(win, text="Mensal por\narquivo", width=16,
                    command=(lambda: os.system("python relatorio2.py "+lb1.get(lb1.curselection()[0]).split(" - ")[2])))
        b6.grid(row=6, column=1)
        b7 = Button(win, text="Total\nUsuário", width=16, command=(
            lambda: os.system("python relatorio3.py "+lb1.get(lb1.curselection()[0]).split(" - ")[2])))
        b7.grid(row=6, column=2)
        b8 = Button(win, text="Total\nEscritorio", width=16, command=(
            lambda: os.system("python relatorio4.py "+lb1.get(lb1.curselection()[0]).split(" - ")[2])))
        b8.grid(row=6, column=3)


def callUI(cfgSets):
    win = Tk()
    win.geometry("505x372")
    app = ConfigFrame(win, cfgSets)
    win.mainloop()


cfgSets = getConfigSets()
callUI(cfgSets)
