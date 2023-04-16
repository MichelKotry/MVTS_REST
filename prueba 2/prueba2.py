from flask import Flask, jsonify, request
from flask_restful import Resource, Api
from conductor import Conductor
from vehiculo import Vehiculo
from mina import Mina
app = Flask(__name__)
api = Api(app)

personas_lista = []

class Personas(Resource):
    def get(self, valor):
        for persona in personas_lista:
            if persona['nombre'] == valor:
                return {'persona buscada': persona}
        return {'resultado': 'persona no encontrada'}

    def post(self):
        persona = request.get_json()
        personas_lista.append(persona)
        return {'resultado': 'persona añadida correctamente'}
    
    def put(self, valor):
        for persona in personas_lista:
            if persona['nombre'] == valor:
                nuevo_nombre = request.json.get('nombre', persona['nombre'])
                persona['nombre'] = nuevo_nombre
                return {'resultado': 'persona modificada correctamente'}
        return {'resultado': 'persona no encontrada'}

    def delete(self, valor):
        for indice, persona in enumerate(personas_lista):
            if persona['nombre'] == valor:
                personas_lista.pop(indice)
                return {'resultado': 'persona borrada correctamente'}

   
    
class Listar(Resource):
    def get(self):
        return jsonify({'personas': personas_lista})
    
api.add_resource(Personas, '/persona/<string:valor>', '/persona/')
api.add_resource(Listar, '/listar')
api.add_resource(Conductor, '/conductor/<string:valor>', '/conductor/')
api.add_resource(Vehiculo, '/vehiculo/<string:valor>', '/vehiculo/')
api.add_resource(Mina, '/mina/<string:valor>', '/mina/')


if __name__ == '__main__':
    app.run(debug=True)
    