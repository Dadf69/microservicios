import requests
import pytest

from conexion import mi_cursor, mi_db

class Test_autores:

    def setup_class(self):
        self.url = "http://localhost:5002/autores"
     
        mi_cursor.execute("INSERT INTO autores (idAutor, nombre, email, idPais) VALUES ('T01', 'Autor Prueba', 'test@mail.com', 'CO')")
        mi_db.commit()

    def teardown_class(self):
       
        mi_cursor.execute("DELETE FROM autores WHERE idAutor IN ('T01', 'T02')")
        mi_db.commit()

   
    def test_lista(self):
        calculado = requests.get(self.url)
        assert calculado.status_code == 200
        assert calculado.json()["mensaje"] == "autores"

    
    @pytest.mark.parametrize(
        ["nuevo", "esperado"],
        [({"idAutor": "T02", "nombre": "Nuevo", "email": "n@m.com", "idPais": "CO"}, "Autor agregado con éxito"),
         ({"idAutor": "T01", "nombre": "Existente", "email": "e@m.com", "idPais": "CO"}, "Id de autor ya existe")]
    )
    def test_agregar(self, nuevo, esperado):
        calculado = requests.post(self.url, json=nuevo)
        assert esperado == calculado.json()["mensaje"]

   
    @pytest.mark.parametrize(
        ["id", "esperado"],
        [("T01", "Autor encontrado"),
         ("FAIL99", "Autor no encontrado")]
    )
    def test_busqueda(self, id, esperado):
        calculado = requests.get(f"{self.url}/{id}")
        assert esperado in calculado.json()["mensaje"]

  
    @pytest.mark.parametrize(
        ["id", "esperado"],
        [("T02", "Autor eliminado con éxito!"),
         ("FAIL99", "Autor no existe")]
    )
    def test_elimina(self, id, esperado):
        calculado = requests.delete(f"{self.url}/{id}")
        assert esperado in calculado.json()["mensaje"]
    
    
    @pytest.mark.parametrize(
        ["id", "datos", "esperado"],
        [("T01", {"idAutor": "T01", "nombre": "Editado", "email": "edit@m.com", "idPais": "CO"}, "Autor modificado con éxito"),
         ("FAIL99", {"idAutor": "FAIL99", "nombre": "Editado", "email": "edit@m.com", "idPais": "CO"}, "Autor no existe")]
    )
    def test_modificar(self, id, datos, esperado):
        calculado = requests.put(f"{self.url}/{id}", json=datos)
        assert esperado in calculado.json()["mensaje"]