import requests
import pytest
from conexion import mi_cursor, mi_db

class Test_paises:

    def setup_class(self):
        self.url = "http://localhost:5001/paises"
        # Limpiar cualquier dato previo
        try:
            mi_cursor.execute("DELETE FROM paises WHERE idPais IN ('T1', 'T2')")
            mi_db.commit()
        except:
            pass
        
        mi_cursor.execute("INSERT INTO paises (idPais, nombre, continente) VALUES ('T1', 'Pais Prueba', 'Continente Prueba')")
        mi_db.commit()

    def teardown_class(self):
     
        mi_cursor.execute("DELETE FROM paises WHERE idPais IN ('T1', 'T2')")
        mi_db.commit()


    def test_lista(self):
        calculado = requests.get(self.url)
        assert calculado.status_code == 200
        assert calculado.json()["mensaje"] == "paises"

    
    @pytest.mark.parametrize(
        ["nuevo", "esperado"],
        [({"idPais": "T2", "nombre": "Nuevo", "continente": "America"}, "Pais agregado con exito"),
         ({"idPais": "T1", "nombre": "Existente", "continente": "Europa"}, "Id de pais ya existe")]
    )
    def test_agregar(self, nuevo, esperado):
        calculado = requests.post(self.url, json=nuevo)
        assert esperado == calculado.json()["mensaje"]

    
    @pytest.mark.parametrize(
        ["id", "esperado"],
        [("T1", "Pais encontrado"),
         ("F9", "Pais no encontrado")]
    )
    def test_busqueda(self, id, esperado):
        calculado = requests.get(f"{self.url}/{id}")
        assert esperado in calculado.json()["mensaje"]

   
    @pytest.mark.parametrize(
        ["id", "esperado"],
        [("T2", "Pais eliminado con exito!"),
         ("F9", "Pais no existe")]
    )
    def test_elimina(self, id, esperado):
        calculado = requests.delete(f"{self.url}/{id}")
        assert esperado in calculado.json()["mensaje"]

   
    @pytest.mark.parametrize(
        ["id", "datos", "esperado"],
        [("T1", {"nombre": "Editado", "continente": "Asia"}, "Pais modificado con exito"),
         ("FAIL99", {"nombre": "Editado", "continente": "Asia"}, "Pais no existe")]
    )
    def test_modificar(self, id, datos, esperado):
        calculado = requests.put(f"{self.url}/{id}", json=datos)
        assert esperado in calculado.json()["mensaje"]