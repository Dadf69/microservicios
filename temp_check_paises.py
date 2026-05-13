import mysql.connector

conn = mysql.connector.connect(host='localhost', port=3306, user='root', password='', database='biblioteca')
cursor = conn.cursor()
cursor.execute("SELECT idPais, nombre FROM paises WHERE idPais IN ('XX','CO')")
print(cursor.fetchall())
conn.close()
