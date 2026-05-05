from conexion import conectar

class AutoresMetodos:
    def listar(self):
        db = conectar()
        cursor = db.cursor(dictionary=True)
        cursor.execute("SELECT * FROM autores")
        res = cursor.fetchall()
        db.close()
        return res

    def consultar(self, id):
        db = conectar()
        cursor = db.cursor(dictionary=True)
        cursor.execute("SELECT * FROM autores WHERE idAutor = %s", (id,))
        res = cursor.fetchall()
        db.close()
        return res

    def agregar(self, id, nombre, email, idp):
        db = conectar()
        cursor = db.cursor()
        cursor.execute("INSERT INTO autores (idAutor, nombre, email, idPais) VALUES (%s, %s, %s, %s)", (id, nombre, email, idp))
        db.commit()
        db.close()

    def modificar(self, id, nombre, email, idp):
        db = conectar()
        cursor = db.cursor()
        cursor.execute("UPDATE autores SET nombre = %s, email = %s, idPais = %s WHERE idAutor = %s", (nombre, email, idp, id))
        db.commit()
        db.close()

    def eliminar(self, id):
        db = conectar()
        cursor = db.cursor()
        cursor.execute("DELETE FROM autores WHERE idAutor = %s", (id,))
        db.commit()
        db.close()