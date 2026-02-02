import pymysql
conn = pymysql.connect(
    host="localhost",
    user="your_user_name",
    password="SQL_password",
    database="database_name"
)
cursor = conn.cursor()
 
class Data:
    def info(self):
        g='''SELECT * FROM RECORD'''
        cursor.execute(g)
        g=cursor.fetchall()
        for information in g:
            print(information)
d=Data()
d.info()
conn.commit()
conn.close()
