import requests
import pytest
from conexion import mi_cursor, mi_db

class Test_editoriales:

    def setup_class(self):
        self.url = "http://localhost:5003/editoriales"
       
        mi_cursor.execute("INSERT INTO editoriales (idEditorial, nombre, idPais) VALUES ('EDT01', 'Editorial Base', 'CO')")
        mi_db.commit()

    def teardown_class(self):
        mi_cursor.execute("DELETE FROM editoriales WHERE idEditorial IN ('EDT01', 'EDT02')")
        mi_db.commit()

    
    def test_lista(self):
        calculado = requests.get(self.url)
        assert calculado.status_code == 200
        assert calculado.json()["mensaje"] == "editoriales"


    @pytest.mark.parametrize(
        ["nuevo", "esperado"],
        [({"idEditorial": "EDT02", "nombre": "Nueva", "idPais": "CO"}, "Editorial agregada con éxito"),
         ({"idEditorial": "EDT01", "nombre": "Repetida", "idPais": "CO"}, "Id de editorial ya existe")]
    )
    def test_agregar(self, nuevo, esperado):
        calculado = requests.post(self.url, json=nuevo)
        assert esperado == calculado.json()["mensaje"]

    
    @pytest.mark.parametrize(
        ["id", "esperado"],
        [("EDT01", "Editorial encontrada"),
         ("999X", "Editorial no encontrada")]
    )
    def test_busqueda(self, id, esperado):
        calculado = requests.get(f"{self.url}/{id}")
        assert esperado in calculado.json()["mensaje"]


    @pytest.mark.parametrize(
        ["id", "esperado"],
        [("EDT02", "Editorial eliminada con éxito!"),
         ("999X", "Editorial no existe")]
    )
    def test_elimina(self, id, esperado):
        calculado = requests.delete(f"{self.url}/{id}")
        assert esperado in calculado.json()["mensaje"]
    

    @pytest.mark.parametrize(
        ["id", "datos", "esperado"],
        [("EDT01", {"idEditorial": "EDT01", "nombre": "Editada", "idPais": "CO"}, "Editorial modificada con éxito"),
         ("999X", {"idEditorial": "999X", "nombre": "Editada", "idPais": "CO"}, "Editorial no existe")]
    )
    def test_modificar(self, id, datos, esperado):
        calculado = requests.put(f"{self.url}/{id}", json=datos)
        assert esperado in calculado.json()["mensaje"]