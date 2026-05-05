import mysql.connector

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="biblioteca"
)

cursor = conn.cursor()

try:
    cursor.execute("DELETE FROM paises")
    conn.commit()
    print("Tabla paises limpiada correctamente")
except Exception as e:
    print(f"Error al limpiar: {e}")

cursor.close()
conn.close()
