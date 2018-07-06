from tkinter import *
from Login import *


class MyMenu(Frame):
    def __init__(self, master):
        super().__init__(master)

        self.menubar = Menu(self)
        self.filemenu = Menu(self.menubar, tearoff=0)
        self.filemenu.add_command(label="Registration")
        self.filemenu.add_command(label="Login", command=self.log)
        self.filemenu.add_command(label="Save")
        self.filemenu.add_command(label="Save as")
        self.filemenu.add_command(label="Close")

        self.filemenu.add_separator()

        self.filemenu.add_command(label="Exit", command=root.quit, accelerator='Ctrl+q')
        self.menubar.add_cascade(label='File', underline=1, menu=self.filemenu)

        self.editmenu = Menu(self.menubar, tearoff=0)
        self.editmenu.add_command(label='Undo')
        self.editmenu.add_separator()

        self.editmenu.add_command(label='Cut')
        self.editmenu.add_command(label='Copy')
        self.editmenu.add_command(label='Paste')
        self.editmenu.add_command(label='Delete')
        self.menubar.add_cascade(label='Edit', underline=0, menu=self.editmenu)

        self.helpmenu = Menu(self.menubar, tearoff=0)
        self.helpmenu.add_command(label='Help Index')
        self.helpmenu.add_command(label='About')
        self.menubar.add_cascade(label='Help', underline=0, menu=self.helpmenu)

    def log(self):
        rt = Tk()
        ob = Login(rt)
        rt.title('Login')
        rt.geometry('300x300')
        rt.mainloop()


root = Tk()
my = MyMenu(root)
root.config(menu=my.menubar)
root.title('My Menu')
root.state('zoomed')  # full screen
# root.geometry('300x300')
root.mainloop()
