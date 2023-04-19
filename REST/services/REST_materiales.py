from flask import Flask, jsonify, request,abort
from flask_restful import Resource, Api

materiales_lista=[]

class REST_Materiales(Resource):
    def get(self, valor):
        for material in materiales_lista:
            if material['id'] == valor:
                return {'material   buscado': material}
        abort(404, description="material no encontrado")  

    def get(self):
        return jsonify({'Materiales': materiales_lista})

    def post(self):
        material = request.get_json()
        materiales_lista.append(material)
        return {'resultado': 'material añadido correctamente'}
    
    def put(self, valor):
        for material in materiales_lista:
            if material['id'] == valor:
                nuevo_nombre = request.json.get('id', material['id'])
                material['id'] = nuevo_nombre
                return {'resultado': 'material modificado correctamente'}
        abort(404, description="material no encontrado")  

    def delete(self, valor):
        for indice, material in enumerate(materiales_lista):
            if material['id'] == valor:
                materiales_lista.pop(indice)
                return {'resultado': 'material borrado correctamente'}
        abort(404, description="material no encontrado")    