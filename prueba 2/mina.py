from flask import Flask, jsonify, request,abort
from flask_restful import Resource, Api

mina_lista=[]

class Mina(Resource):
    def get(self, valor):
        for mina in mina_lista:
            if mina['id'] == valor:
                return {'mina   buscada': mina}
        abort(404, description="mina no encontrada")  

    def get(self):
        return jsonify({'Minas': mina_lista})
    
    def post(self):
        mina = request.get_json()
        mina_lista.append(mina)
        return {'resultado': 'mina añadida correctamente'}
    
    def put(self, valor):
        for mina in mina_lista:
            if mina['id'] == valor:
                nuevo_nombre = request.json.get('id', mina['id'])
                mina['id'] = nuevo_nombre
                return {'resultado': 'mina modificada correctamente'}
        abort(404, description="mina no encontrada")  

    def delete(self, valor):
        for indice, persona in enumerate(mina_lista):
            if persona['nombre'] == valor:
                mina_lista.pop(indice)
                return {'resultado': 'mina borrada correctamente'}
        abort(404, description="mina no encontrada")    