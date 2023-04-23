from flask import Flask, jsonify, request,abort
from flask_restful import Resource, Api
from models.models import Semaforo
from controls import ControlSemaforo

class REST_Semaforo(Resource):
    def __init__(self):
        self.control_semaforo= ControlSemaforo()
            
    def get(self, id=None):
        if id is None:
            semaforos = self.control_semaforo.get_all()
            semaforos_dicts = [semaforo.__dict__ for semaforo in semaforos]
            for semaforo_dict in semaforos_dicts:
                if '_sa_instance_state' in semaforo_dict:
                    del semaforo_dict['_sa_instance_state']
            return jsonify(semaforos_dicts)
        else:
            semaforo = self.control_semaforo.get(int(id))
            if semaforo:
                semaforo_dict = semaforo.__dict__
                if '_sa_instance_state' in semaforo_dict:
                    del semaforo_dict['_sa_instance_state']
                return jsonify(semaforo_dict)
            abort(404, description="semaforo no encontrado")

    def post(self):
        semaforo_data = request.get_json()
        print(semaforo_data)
        semaforo = Semaforo(fecha_hora=semaforo_data['fecha_hora'], 
                      duracion=semaforo_data['duracion'], 
                      ubicacion_id=semaforo_data['ubicacion_id'], 
                      semaforo_id=semaforo_data['semaforo_id']) 
                      
        print(semaforo)
        self.control_semaforo.create(semaforo)
        return {'resultado': 'semaforo añadido correctamente'}
    
    def put(self, id):
        semaforo_data = request.get_json()
        semaforo = self.control_semaforo.get(id)
        if not semaforo:
            abort(404, message="semaforo no encontrado")

        if 'fecha_hora' in semaforo_data:
            semaforo.fecha_hora = semaforo_data['fecha_hora']
        if 'duracion' in semaforo_data:
            semaforo.duracion = semaforo_data['duracion']
        if 'ubicacion_id' in semaforo_data:
            semaforo.ubicacion_id = semaforo_data['ubicacion_id']
        if 'semaforo_id' in semaforo_data:
            semaforo.semaforo_id = semaforo_data['semaforo_id']

        self.control_semaforo.update(semaforo)
        return jsonify({'resultado': 'semaforo modificado correctamente'})

    def delete(self, id):
        semaforo = self.control_semaforo.get(id)
        if not semaforo:
            abort(404, message="semaforo no encontrado")
        self.control_semaforo.delete(semaforo)
        return jsonify({'resultado': 'semaforo borrado correctamente'})
  