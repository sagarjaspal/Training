from tkinter import *
from tkinter import messagebox as tm


class Demo(Frame):
    def __init__(self, other):
        super().__init__(other)

        self.lblName = Label(self, text='Name')
        self.txtName = Entry(self)

        self.btnOk = Button(self, text='OK', command=self.show)

        self.lblName.grid(row=0, column=0)
        self.txtName.grid(row=0, column=1)

        self.btnOk.grid(columnspan=2)

        self.pack()

    def show(self):
        name = self.txtName.get()
        tm.showinfo('Greetings!', 'Hello ' + name)


root = Tk()
ob = Demo(root)
root.title('Student')
root.geometry('300x300')
root.mainloop()
