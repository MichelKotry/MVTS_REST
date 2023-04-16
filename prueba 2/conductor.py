
from flask import Flask, jsonify, request
from flask_restful import Resource, Api

conductor_lista=[]

class Conductor(Resource):
    def get(self, valor):
        for persona in conductor_lista:
            if persona['nombre'] == valor:
                return {'conductor buscado': persona}
        return {'resultado': 'conductor no encontrado'}

    def post(self):
        persona = request.get_json()
        conductor_lista.append(persona)
        return {'resultado': 'conductor añadido correctamente'}
    
    def put(self, valor):
        for persona in conductor_lista:
            if persona['nombre'] == valor:
                nuevo_nombre = request.json.get('nombre', persona['nombre'])
                persona['nombre'] = nuevo_nombre
                return {'resultado': 'conductor modificado correctamente'}
        return {'resultado': 'conductor no encontrado'}

    def delete(self, valor):
        for indice, persona in enumerate(conductor_lista):
            if persona['nombre'] == valor:
                conductor_lista.pop(indice)
                return {'resultado': 'conductor borrado correctamente'}

