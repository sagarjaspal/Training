from tkinter import *
from PIL import ImageTk,Image
root = Tk()
root.title('Image Box')
root.geometry('400x500')
path = 'test.jpeg'
img = ImageTk.PhotoImage(Image.open(path))
imglbl = Label(root, image=img)
imglbl.pack(side='bottom', fill='both', expand='yes')
root.mainloop()
