from tkinter import *

labelUser = "usuario"


class ConfigFrame(Frame):

    def __init__(self, win):
        super().__init__()
        self.win = win
        self.initUI(win)

    def initUI(self, win):

        self.master.title("Arch-Timer 1.0")

        l0 = Label(win, text="Cadastro/Usuário")
        l0.grid(row=0, column=0, columnspan=4)

        l1 = Label(win, textvariable=labelUser)
        l1.grid(row=1, column=0, columnspan=3)
        b1 = Button(win, text="Mudar usuário", width=12)
        b1.grid(row=1, column=3)
        lb1 = Listbox(win, width=45, height=16)
        lb1.grid(row=2, column=0, rowspan=3, columnspan=3)
        b2 = Button(win, text="Adicionar\nCliente", height=5, width=12)
        b2.grid(row=2, column=3)
        b3 = Button(win, text="Mudar\nCliente", height=5, width=12)
        b3.grid(row=3, column=3)
        b4 = Button(win, text="Remover\nCliente", height=5, width=12)
        b4.grid(row=4, column=3)

        l2 = Label(win, text="Relatórios")
        l2.grid(row=5, column=0, columnspan=4)
        b5 = Button(win, text="Mensal Usuário", width=12)
        b5.grid(row=6, column=0)
        b6 = Button(win, text="Mensal Total", width=12)
        b6.grid(row=6, column=1)
        b7 = Button(win, text="Total Usuário", width=12)
        b7.grid(row=6, column=2)
        b8 = Button(win, text="Total", width=12)
        b8.grid(row=6, column=3)


def callUI():
    win = Tk()
    win.geometry("380x359")
    app = ConfigFrame(win)
    win.mainloop()


callUI()
