from flask import Flask, jsonify, request,abort
from flask_restful import Resource, Api

ordenes_listaMat=[]

class OrdenesMateriales(Resource):
    def get(self, valor):
        for orden in ordenes_listaMat:
            if orden['id'] == valor:
                return {'orden buscada': orden}
        abort(404, description="orden no encontrada")  

    def get(self):
        return jsonify({'Ordenes': ordenes_listaMat})

    def post(self):
        orden = request.get_json()
        ordenes_listaMat.append(orden)
        return {'resultado': 'orden añadida correctamente'}
    
    def put(self, valor):
        for orden in ordenes_listaMat:
            if orden['id'] == valor:
                nuevo_nombre = request.json.get('id', orden['id'])
                orden['id'] = nuevo_nombre
                return {'resultado': 'orden modificada correctamente'}
        abort(404, description="orden no encontrada")  

    def delete(self, valor):
        for indice, orden in enumerate(ordenes_listaMat):
            if orden['id'] == valor:
                ordenes_listaMat.pop(indice)
                return {'resultado': 'orden borrada correctamente'}
        abort(404, description="orden no encontrada")    