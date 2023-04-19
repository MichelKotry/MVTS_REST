from flask import Flask, jsonify, request,abort
from flask_restful import Resource, Api

Ubicaciones_lista=[]

class REST_Ubicaciones(Resource):
    def get(self, valor):
        for ubicacion in Ubicaciones_lista:
            if ubicacion['id'] == valor:
                return {'ubicacion buscada': ubicacion}
        abort(404, description="ubicacion no encontrada")  

    def get(self):
        return jsonify({'Ubicaciones': Ubicaciones_lista})

    def post(self):
        ubicacion = request.get_json()
        Ubicaciones_lista.append(ubicacion)
        return {'resultado': 'ubicacion añadida correctamente'}
    
    def put(self, valor):
        for ubicacion in Ubicaciones_lista:
            if ubicacion['id'] == valor:
                nuevo_nombre = request.json.get('id', ubicacion['id'])
                ubicacion['id'] = nuevo_nombre
                return {'resultado': 'ubicacion modificada correctamente'}
        abort(404, description="ubicacion no encontrada")  

    def delete(self, valor):
        for indice, ubicacion in enumerate(Ubicaciones_lista):
            if ubicacion['id'] == valor:
                Ubicaciones_lista.pop(indice)
                return {'resultado': 'ubicacion borrada correctamente'}
        abort(404, description="ubicacion no encontrada")    