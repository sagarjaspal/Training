from tkinter import *
from tkinter import messagebox as tm
from pymysql import *


class Demo(Frame):
    def __init__(self, other):
        super().__init__(other)

        self.con = connect(db='test', user='root', password='', host='localhost')

        self.lblNo = Label(self, text='Employee Number')
        self.lblName = Label(self, text='Employee Name')
        self.lblSalary = Label(self, text='Salary')

        self.txtNo = Entry(self)
        self.txtName = Entry(self)
        self.txtSalary = Entry(self)

        self.btnSave = Button(self, text='Save', command=self.save)
        self.btnSearch = Button(self, text='Search', command=self.search)
        self.btnExit = Button(self, text='Exit')

        self.lblNo.grid(row=0, column=0)
        self.txtNo.grid(row=0, column=1)
        self.lblName.grid(row=1, column=0)
        self.txtName.grid(row=1, column=1)
        self.lblSalary.grid(row=2, column=0)
        self.txtSalary.grid(row=2, column=1)
        self.btnSave.grid(row=3, column=0)
        self.btnSearch.grid(row=3, column=1)
        self.btnExit.grid(row=3, column=2)

        self.pack()

    def save(self):
        cur = self.con.cursor()
        eno = int(self.txtNo.get())
        name = self.txtName.get()
        salary = int(self.txtSalary.get())
        cur.execute("insert into emp values(%d, '%s', %f)" % (eno, name, salary))
        self.con.commit()
        self.txtNo.delete(0, 'end')  # removes data in text field
        self.txtName.delete(0, 'end')
        self.txtSalary.delete(0, 'end')
        self.txtNo.focus()  # cursor comes back to text field connected to this object

    def search(self):
        eno = int(self.txtNo.get())
        cur = self.con.cursor()
        x = cur.execute("select * from emp where eno = %d" % eno)

        if x:
            result = cur.fetchone()
            self.txtName.delete(0, 'end')
            self.txtSalary.delete(0, 'end')
            self.txtName.insert(0, result[1])
            self.txtSalary.insert(0, result[2])
        else:
            tm.showinfo('Error', 'Record not found')


root = Tk()
obj = Demo(root)
root.title('Employee')
root.geometry('300x300')
root.mainloop()
