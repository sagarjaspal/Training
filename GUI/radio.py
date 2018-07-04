from tkinter import *


class Demo(Frame):
    def __init__(self, abc):
        super().__init__(abc)

        self.var = StringVar(value=False)

        self.R1 = Radiobutton(self, text='Python', variable=self.var,
                              value='Python', command=self.sel)
        self.R1.pack(anchor=W)
        self.R2 = Radiobutton(self, text='DS', variable=self.var,
                              value='DS', command=self.sel)
        self.R2.pack(anchor=W)
        self.R3 = Radiobutton(self, text='ML', variable=self.var,
                              value='ML', command=self.sel)
        self.R3.pack(anchor=W)

        self.lbl = Label(self)
        self.lbl.pack()
        self.pack()

    def sel(self):
        selection = "You selected " + str(self.var.get())
        self.lbl.config(text=selection)


root = Tk()
obj = Demo(root)
root.title('Select Technology')
root.geometry('300x300')
root.mainloop()
