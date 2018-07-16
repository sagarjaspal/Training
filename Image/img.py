from tkinter import *
root = Tk()
c = Canvas(root, bg='green', height=500, width=500)
filename = PhotoImage(file='test.png')
bg_label = Label(root, image=filename)
bg_label.place(x=0, y=0, relwidth=1, relheight=1)
c.pack()
root.mainloop()
