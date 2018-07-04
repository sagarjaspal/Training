from tkinter import *


class Login(Frame):
    def __init__(self, master):
        super().__init__(master)

        self.lblId = Label(self, font=('algerian', 15, 'bold'),
                           text='User Name', fg='Steel Blue', bd=10)

        self.lblPass = Label(self, font=('algerian', 15, 'bold'),
                             text='Password', fg='Steel Blue', bd=10)

        self.txtId = Entry(self, font=('arial', 16, 'bold'), bd=10, fg='blue',
                           insertwidth=4, bg='powder blue', justify='center')

        self.txtPass = Entry(self, font=('arial', 16, 'bold'), bd=10, fg='blue',
                             insertwidth=4, bg='powder blue', justify='center', show='*')

        self.lblId.grid(row=0, column=0)
        self.txtId.grid(row=0, column=1)

        self.lblPass.grid(row=1, column=0)
        self.txtPass.grid(row=1, column=1)

        self.btnLogin = Button(self, padx=20, pady=8, bd=16, fg='black',
                               font=('arial', 16, 'bold'), width=8, text='Login',
                               bg='powder blue')
        self.btnExit = Button(self, padx=20, pady=8, bd=16, fg='black',
                              font=('arial', 16, 'bold'), width=8, text='Exit',
                              bg='powder blue')

        self.btnLogin.grid(row=2, column=0)
        self.btnExit.grid(row=2, column=1)

        self.pack()


root = Tk()
log = Login(root)
root.title('Login Box')
root.geometry('300x300')
root.mainloop()
