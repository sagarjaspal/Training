import pymysql


class Demo:
    def save(self):
        con = pymysql.connect(db='test', user='root', password='', host='localhost')
        cur = con.cursor()
        cur.execute("select * from emp")
        result = cur.fetchall()
        print(result)
        result = cur.fetchmany(3)
        print(result)
        result = cur.fetchone()
        print(result)
        con.close()


d = Demo()
d.save()
