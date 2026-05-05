from conexion import conectar

class EditorialesMetodos:
    def listar(self):
        db = conectar()
        cursor = db.cursor(dictionary=True)
        cursor.execute("SELECT * FROM editoriales")
        res = cursor.fetchall()
        db.close()
        return res

    def consultar(self, id):
        db = conectar()
        cursor = db.cursor(dictionary=True)
        cursor.execute("SELECT * FROM editoriales WHERE idEditorial = %s", (id,))
        res = cursor.fetchall()
        db.close()
        return res

    def agregar(self, id, nombre, idp):
        db = conectar()
        cursor = db.cursor()
        cursor.execute("INSERT INTO editoriales (idEditorial, nombre, idPais) VALUES (%s, %s, %s)", (id, nombre, idp))
        db.commit()
        db.close()

    def modificar(self, id, nombre, idp):
        db = conectar()
        cursor = db.cursor()
        cursor.execute("UPDATE editoriales SET nombre = %s, idPais = %s WHERE idEditorial = %s", (nombre, idp, id))
        db.commit()
        db.close()

    def eliminar(self, id):
        db = conectar()
        cursor = db.cursor()
        cursor.execute("DELETE FROM editoriales WHERE idEditorial = %s", (id,))
        db.commit()
        db.close()
