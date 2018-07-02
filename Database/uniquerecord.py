import pymysql


class Demo:
    def save(self):
        con = pymysql.connect(db='test', user='root', password='', host='localhost')
        cur = con.cursor()
        eno = int(input('Enter no.: '))
        name = input('Enter name: ')
        sal = float('Enter salary: ')
        x = cur.execute("select * from emp where eno = %d") % eno
        if x:
            print('Duplicate')

        else:
            cur.execute("insert into emp values (%d, '%s', %f)" % (eno, name, sal))
            con.commit()
            print('Record Saved')
            con.close()


d = Demo()
d.save()








