from flask import Flask, jsonify, request,abort
from flask_restful import Resource, Api

Congestiones_lista=[]

class Congestiones(Resource):
    def get(self, valor):
        for congestion in Congestiones_lista:
            if congestion['id'] == valor:
                return {'congestion buscada': congestion}
        abort(404, description="congestion no encontrada")  

    def get(self):
        return jsonify({'Congestiones': Congestiones_lista})

    def post(self):
        congestion = request.get_json()
        Congestiones_lista.append(congestion)
        return {'resultado': 'congestion añadida correctamente'}
    
    def put(self, valor):
        for congestion in Congestiones_lista:
            if congestion['id'] == valor:
                nuevo_nombre = request.json.get('id', congestion['id'])
                congestion['id'] = nuevo_nombre
                return {'resultado': 'congestion modificada correctamente'}
        abort(404, description="congestion no encontrada")  

    def delete(self, valor):
        for indice, congestion in enumerate(Congestiones_lista):
            if congestion['id'] == valor:
                Congestiones_lista.pop(indice)
                return {'resultado': 'congestion borrada correctamente'}
        abort(404, description="congestion no encontrada")    