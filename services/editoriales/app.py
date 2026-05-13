from flask import Flask, request, jsonify
from flask_restful import Resource, Api
from editoriales import EditorialesMetodos 

programa = Flask(__name__)
api = Api(programa)
mis_editoriales = EditorialesMetodos()

class ListaEditoriales(Resource):
    def get(self):
        editoriales = mis_editoriales.listar()
        return {"mensaje": "editoriales", "data": editoriales}
    
    def post(self):
        nuevo = request.json
        resultado = mis_editoriales.consultar(nuevo["idEditorial"])
        if len(resultado) == 0:
            if not mis_editoriales.pais_existe(nuevo["idPais"]):
                return {"mensaje": "Pais no existe"}, 200
            mis_editoriales.agregar(nuevo["idEditorial"], nuevo["nombre"], nuevo["idPais"])
            return {"mensaje": "Editorial agregada con éxito"}, 201
        else:
            return {"mensaje": "Id de editorial ya existe"}, 200

class Editorial(Resource):
    def get(self, id):
        resultado = mis_editoriales.consultar(id)
        if len(resultado) == 0:
            return {"mensaje": "Editorial no encontrada"}, 404
        else:
            return {"mensaje": "Editorial encontrada", "editorial": resultado[0]}, 200
    
    def delete(self, id):
        resultado = mis_editoriales.consultar(id)
        if len(resultado) == 0:
            return {"mensaje": "Editorial no existe"}, 200
        else:
            mis_editoriales.eliminar(id)
            return {"mensaje": "Editorial eliminada con éxito!"}, 200
    
    def put(self, id):
        resultado = mis_editoriales.consultar(id)
        if len(resultado) == 0:
            return {"mensaje": "Editorial no existe"}, 200
        else:
            nuevo = request.json
            if not mis_editoriales.pais_existe(nuevo["idPais"]):
                return {"mensaje": "Pais no existe"}, 200
            mis_editoriales.modificar(id, nuevo["nombre"], nuevo["idPais"])
            return {"mensaje": "Editorial modificada con éxito"}, 200

api.add_resource(ListaEditoriales, "/editoriales")
api.add_resource(Editorial, "/editoriales/<id>")

if __name__ == "__main__":
    programa.run(host="0.0.0.0", debug=True, port=5003)