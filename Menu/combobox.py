from tkinter import *


class Combo(Frame):
    def __init__(self, master):
        super().__init__(master)

        self.var = StringVar(self)
        choices = {'Python', 'ML', 'DS', 'Django'}
        self.var.set('Python')
        self.popupMenu = OptionMenu(self, self.var, *choices)
        self.lbl = Label(self, text='Choose a language')
        self.lbl.grid(row=1, column=1)
        self.popupMenu.grid(row=2, column=1)
        self.pack()


root = Tk()
ob = Combo(root)
root.title('Combo Box')
root.geometry('200x200')
root.mainloop()
