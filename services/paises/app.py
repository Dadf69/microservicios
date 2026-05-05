from flask import Flask, request
from flask_restful import Resource, Api
from paises import PaisesMetodos

app = Flask(__name__)
api = Api(app)
mis_paises = PaisesMetodos()

class ListaPaises(Resource):
    def get(self):
        paises = mis_paises.listar()
        return {"mensaje": "paises", "data": paises}

    def post(self):
        nuevo = request.json
        resultado = mis_paises.consultar(nuevo["idPais"])
        if len(resultado) == 0:
            mis_paises.agregar(nuevo["idPais"], nuevo["nombre"], nuevo["continente"])
            return {"mensaje": "Pais agregado con exito"}, 201
        else:
            return {"mensaje": "Id de pais ya existe"}, 200

class Pais(Resource):
    def get(self, id):
        resultado = mis_paises.consultar(id)
        if len(resultado) == 0:
            return {"mensaje": "Pais no encontrado"}, 404
        else:
            return {"mensaje": "Pais encontrado", "pais": resultado[0]}, 200

    def delete(self, id):
        resultado = mis_paises.consultar(id)
        if len(resultado) == 0:
            return {"mensaje": "Pais no existe"}, 200
        else:
            mis_paises.eliminar(id)
            return {"mensaje": "Pais eliminado con exito!"}, 200
    
    def put(self, id):
        resultado = mis_paises.consultar(id)
        if len(resultado) == 0:
            return {"mensaje": "Pais no existe"}, 200
        else:
            nuevo = request.json
            mis_paises.modificar(id, nuevo["nombre"], nuevo["continente"])
            return {"mensaje": "Pais modificado con exito"}, 200

api.add_resource(ListaPaises, "/paises")
api.add_resource(Pais, "/paises/<id>")

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True, port=5001)
