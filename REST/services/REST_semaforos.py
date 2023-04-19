from flask import Flask, jsonify, request,abort
from flask_restful import Resource, Api

Semaforo_lista=[]

class REST_Semaforo(Resource):
    def get(self, valor):
        for semaforo in Semaforo_lista:
            if semaforo['id'] == valor:
                return {'semaforo   buscado': semaforo}
        abort(404, description="semaforo no encontrado")  

    def get(self):
        return jsonify({'Semaforos': Semaforo_lista})
    
    def post(self):
        semaforo = request.get_json()
        Semaforo_lista.append(semaforo)
        return {'resultado': 'semaforo añadido correctamente'}
    
    def put(self, valor):
        for semaforo in Semaforo_lista:
            if semaforo['id'] == valor:
                nuevo_nombre = request.json.get('id', semaforo['id'])
                semaforo['id'] = nuevo_nombre
                return {'resultado': 'semaforo modificado correctamente'}
        abort(404, description="semaforo no encontrado")  

    def delete(self, valor):
        for indice, semaforo in enumerate(Semaforo_lista):
            if semaforo['id'] == valor:
                Semaforo_lista.pop(indice)
                return {'resultado': 'semaforo borrado correctamente'}
        abort(404, description="semaforo no encontrado")    