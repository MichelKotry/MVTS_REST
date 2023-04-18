from flask import Flask, jsonify, request,abort
from flask_restful import Resource, Api

personas_lista = []

class Gerentes(Resource):
    def get(self, valor):
        for persona in personas_lista:
            if persona['id'] == valor:
                return {'persona buscada': persona}
        abort(404, description="Persona no encontrada")

    def get(self):
        return jsonify({'Gerentes': personas_lista})
    
    def post(self):
        persona = request.get_json()
        personas_lista.append(persona)
        return {'resultado': 'persona añadida correctamente'}
    
    def put(self, valor):
        for persona in personas_lista:
            if persona['id'] == valor:
                nuevo_nombre = request.json.get('id', persona['id'])
                persona['id'] = nuevo_nombre
                return {'resultado': 'persona modificada correctamente'}
        abort(404, description="Persona no encontrada")

    def delete(self, valor):
        for indice, persona in enumerate(personas_lista):
            if persona['id'] == valor:
                personas_lista.pop(indice)
                return {'resultado': 'persona borrada correctamente'}
        abort(404, description="Persona no encontrada")

