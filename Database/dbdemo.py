from pymysql import *
# step-1: import module


class DbDemo:
    def __init__(self):
        # step-2: create connection object in constructor
        self.con = connect(db='test', user='root', password='', host='localhost')

    def save(self):
        # input values
        eno = int(input('Enter emp no.: '))
        name = input('Enter name: ')
        salary = float(input('Enter salary: '))

        # step-3: create cursor using connection object, execute query using cursor
        cur = self.con.cursor()
        query = "insert into emp values (%d , '%s' , %f)" % (eno, name, salary)
        cur.execute(query)

        # step-4: commit to database using connection object
        self.con.commit()
        print('Record saved')

        # step-5: close the database
        self.con.close()

    def show(self):
        cur = self.con.cursor()
        cur.execute("select * from emp")
        record = cur.fetchall() # saves all content of cursor in the object
        if record:
            print(record)
            print(type(record))
        '''i = 0 
        while i < len(record):
            print('Employee No', record[i][0])
            print('Employee name', record[i][1])
            print('Employee salary', record[i][2])
            print('-------------------------------------')
            i += 1'''


ob = DbDemo()
ob.save()
ob.show()
