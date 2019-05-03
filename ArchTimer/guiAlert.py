from tkinter import *


class alertClass(Frame):

    def __init__(self, winAlert, alertText):
        super().__init__()
        self.winAlert = winAlert
        self.initUI(winAlert, alertText)

    def initUI(self, winAlert, alertText):
        winAlert.title("ATENÇÃO!!!")
        alertTextl1 = StringVar()
        l1 = Label(winAlert, text=alertText)
        # alertTextl1.set(texto)
        l1.pack()
        b1 = Button(winAlert, width=20, text="Ok!",
                    command=lambda: winAlert.destroy())
        b1.pack()


def alertUI(alertText="Erro!"):
    winAlert = Tk()
    winAlert.geometry("250x55")
    app = alertClass(winAlert, alertText)
    winAlert.mainloop()


# alertUI()
