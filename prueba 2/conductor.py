
from flask import Flask, jsonify, request,abort
from flask_restful import Resource, Api

conductor_lista=[]

class Conductor(Resource):
    def get(self, valor):
        for conductor in conductor_lista:
            if conductor['id'] == valor:
                return {'conductor buscado': conductor}
        abort(404, description="conductor no encontrado")

    def get(self):
        return jsonify({'Conductores': conductor_lista})

    def post(self):
        conductor = request.get_json()
        conductor_lista.append(conductor)
        return {'resultado': 'conductor añadido correctamente'}
    
    def put(self, valor):
        for conductor in conductor_lista:
            if conductor['id'] == valor:
                nuevo_nombre = request.json.get('id', conductor['id'])
                conductor['id'] = nuevo_nombre
                return {'resultado': 'conductor modificado correctamente'}
        abort(404, description="conductor no encontrado")

    def delete(self, valor):
        for indice, conductor in enumerate(conductor_lista):
            if conductor['id'] == valor:
                conductor_lista.pop(indice)
                return {'resultado': 'conductor borrado correctamente'}
        abort(404, description="conductor no encontrado")
