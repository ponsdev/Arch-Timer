from tkinter import *
from tkinter import ttk
from classes import *


class changeUser(Frame):

    def __init__(self, win, labelUser):
        super().__init__()
        self.win = win
        self.initUI(win, labelUser)

    def initUI(self, win, labelUser):

        self.master.title("Usuário")
        l1 = Label(win, text="Digite o nome do usuário:")
        l1.grid(row=0, column=0)
        t1 = Text(win, width=30, height=1)
        t1.grid(row=1, column=0)
        b1 = Button(win, width=20, text="Ok!",
                    command=lambda: setUser(win, labelUser, t1.get('1.0', END).strip()))
        b1.grid(row=2, column=0)
        t1.insert("1.0", getUser())


def changeUserUI(labelUser):
    win = Tk()
    win.geometry("250x73")
    app = changeUser(win, labelUser)
    win.mainloop()


class addClientClass(Frame):

    def __init__(self, win, id, lbIn):
        super().__init__()
        self.win = win
        self.initUI(win, id, lbIn)

    def initUI(self, win, id, lbIn):

        self.master.title("Adicionar Cliente")
        l1 = Label(win, text="Nome:")
        l1.grid(row=0, column=0)
        t1 = Text(win, width=25, height=1)
        t1.grid(row=0, column=1)
        l2 = Label(win, text="Código:")
        l2.grid(row=1, column=0)
        t2 = Text(win, width=25, height=1)
        t2.grid(row=1, column=1)
        l3 = Label(win, text="Caminho:")
        l3.grid(row=2, column=0)
        t3 = Text(win, width=25, height=1)
        t3.grid(row=2, column=1)
        b1 = Button(win, width=20, text="Ok!",
                    command=lambda: addClient(win, t1.get('1.0', END).strip(), t2.get('1.0', END).strip(), t3.get('1.0', END).strip(), id, lbIn))
        b1.grid(row=3, column=0, columnspan=2)


def addClientUI(id, lbIn):
    win = Tk()
    # win.geometry("250x73")
    app = addClientClass(win, id, lbIn)
    win.mainloop()


class changeClientClass(Frame):

    def __init__(self, win, item, lbIn, END, id):
        super().__init__()
        self.win = win
        self.initUI(win, item, lbIn, END, id)

    def initUI(self, win, item, lbIn, END, id):
        print(item)
        name = item.split(" - ")[0]
        cod = item.split(" - ")[1].replace("Cod:", "")
        path = item.split(" - ")[2]

        self.master.title("Alterar Cliente")
        l1 = Label(win, text="Nome:")
        l1.grid(row=0, column=0)
        t1 = Text(win, width=25, height=1)
        t1.grid(row=0, column=1)
        t1.insert('1.0', name)
        l2 = Label(win, text="Código:")
        l2.grid(row=1, column=0)
        t2 = Text(win, width=25, height=1)
        t2.grid(row=1, column=1)
        t2.insert('1.0', cod)
        l3 = Label(win, text="Caminho:")
        l3.grid(row=2, column=0)
        t3 = Text(win, width=25, height=1)
        t3.grid(row=2, column=1)
        t3.insert('1.0', path)
        b1 = Button(win, width=20, text="Ok!",
                    command=lambda: changeClient(win, t1.get('1.0', END).strip(), t2.get('1.0', END).strip(), t3.get('1.0', END).strip(), lbIn, END, id, item))
        b1.grid(row=3, column=0, columnspan=2)


def changeClientUI(item, lbIn, END, id):
    win = Tk()
    # win.geometry("250x73")
    app = changeClientClass(win, item, lbIn, END, id)
    win.mainloop()