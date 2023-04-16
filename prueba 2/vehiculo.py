from flask import Flask, jsonify, request
from flask_restful import Resource, Api

vehiculo_lista=[]

class Vehiculo(Resource):
    def get(self, valor):
        for persona in vehiculo_lista:
            if persona['nombre'] == valor:
                return {'conductor buscado': persona}
        return {'resultado': 'persona no encontrada'}

    def post(self):
        persona = request.get_json()
        vehiculo_lista.append(persona)
        return {'resultado': 'conductor añadido correctamente'}
    
    def put(self, valor):
        for persona in vehiculo_lista:
            if persona['nombre'] == valor:
                nuevo_nombre = request.json.get('nombre', persona['nombre'])
                persona['nombre'] = nuevo_nombre
                return {'resultado': 'conductor modificado correctamente'}
        return {'resultado': 'conductor no encontrado'}

    def delete(self, valor):
        for indice, persona in enumerate(vehiculo_lista):
            if persona['nombre'] == valor:
                vehiculo_lista.pop(indice)
                return {'resultado': 'conductor borrado correctamente'}

