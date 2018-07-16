from tkinter import *
import random
root = Tk()

root.geometry('170x200+30+30')
lang = ['Python', 'Perl', 'C++', 'Java', 'Node']
labels = range(5)

for i in range(5):
    ct = [random.randrange(256) for x in range(3)]
    brightness = int(round(0.299*ct[0]) + 0.587*ct[1] + 0.114*ct[2])
    ct_hex = '%02x%02x%02x' % tuple(ct)
    bg_color = '#' + "".join(ct_hex)
    butLbl = Label(root, text=lang[i], fg='White' if brightness<120 else 'Black', bg=bg_color)
    butLbl.place(x=20, y=30+i*30, width=120, height=25)
root.mainloop()
