from flask import Flask, jsonify
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

personas_lista = [
    {
        "nombre": "Juan",
        "apellido": "Pérez",
        "edad": 25
    },
    {
        "nombre": "María",
        "apellido": "García",
        "edad": 30
    },
    {
        "nombre": "Pedro",
        "apellido": "López",
        "edad": 40
    }
]

class Personas(Resource):
    def get(self, valor):
        for persona in personas_lista:
            if persona['nombre'] == valor:
                return {'persona buscada': persona}
        return {'resultado': 'persona no encontrada'}

    def post(self, valor):
        persona = {'nombre': valor}
        personas_lista.append(persona)
        return {'resultado': 'persona añadida correctamente'}

    def delete(self, valor):
        for indice, persona in enumerate(personas_lista):
            if persona['nombre'] == valor:
                personas_lista.pop(indice)
                return {'resultado': 'persona borrada correctamente'}

class Listar(Resource):
    def get(self):
        return jsonify({'personas': personas_lista})

api.add_resource(Personas, '/persona/<string:valor>')
api.add_resource(Listar, '/listar')

if __name__ == '__main__':
    app.run(debug=True)
    