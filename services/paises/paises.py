from conexion import conectar

class PaisesMetodos:
    def listar(self):
        db = conectar()
        cursor = db.cursor(dictionary=True)
        cursor.execute("SELECT * FROM paises")
        res = cursor.fetchall()
        db.close()
        return res

    def consultar(self, id):
        db = conectar()
        cursor = db.cursor(dictionary=True)
        cursor.execute("SELECT * FROM paises WHERE idPais = %s", (id,))
        res = cursor.fetchall()
        db.close()
        return res

    def agregar(self, id, nombre, continente):
        db = conectar()
        cursor = db.cursor()
        cursor.execute("INSERT INTO paises (idPais, nombre, continente) VALUES (%s, %s, %s)", (id, nombre, continente))
        db.commit()
        db.close()

    def modificar(self, id, nombre, continente):
        db = conectar()
        cursor = db.cursor()
        cursor.execute("UPDATE paises SET nombre = %s, continente = %s WHERE idPais = %s", (nombre, continente, id))
        db.commit()
        db.close()

    def eliminar(self, id):
        db = conectar()
        cursor = db.cursor()
        cursor.execute("DELETE FROM paises WHERE idPais = %s", (id,))
        db.commit()
        db.close()
