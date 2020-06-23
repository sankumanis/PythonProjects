
import mysql.connector as connector

conn = connector.connect(user='sanku', password='lipi98',
                              host='127.0.0.1',
                              database='sanku_db')

cur = conn.cursor()

cur.execute('select * from customer')
data = cur.fetchall()

conn.close()

for row in data:
    print(row)

