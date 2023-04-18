from flask import Flask, jsonify, request,abort
from flask_restful import Resource, Api

vehiculo_lista=[]

class Vehiculo(Resource):
    def get(self, valor):
        for vehiculo in vehiculo_lista:
            if vehiculo['id'] == valor:
                return {'veiculo buscado': vehiculo}
        abort(404, description="vehiculo no encontrado")  

    def get(self):
        return jsonify({'personas': vehiculo_lista})

    def post(self):
        vehiculo = request.get_json()
        vehiculo_lista.append(vehiculo)
        return {'resultado': 'vehiculo añadido correctamente'}
    
    def put(self, valor):
        for vehiculo in vehiculo_lista:
            if vehiculo['id'] == valor:
                nuevo_nombre = request.json.get('id', vehiculo['id'])
                vehiculo['id'] = nuevo_nombre
                return {'resultado': 'vehiculo modificado correctamente'}
        abort(404, description="vehiculo no encontrada")  

    def delete(self, valor):
        for indice, vehiuculo in enumerate(vehiculo_lista):
            if vehiuculo['id'] == valor:
                vehiculo_lista.pop(indice)
                return {'resultado': 'vehiculo borrado correctamente'}
        abort(404, description="vehiculo no encontrada")  
