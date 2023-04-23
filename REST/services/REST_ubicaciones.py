from flask import Flask, jsonify, request,abort
from flask_restful import Resource, Api
from models.models import Ubicacion
from controls import ControlUbicacion

class REST_Ubicaciones(Resource):
    def __init__(self):
        self.control_ubicacion = ControlUbicacion()
            
    def get(self, id=None):
        if id is None:
            ubicaciones = self.control_ubicacion.get_all()
            ubicaciones_dicts = [ubicacion.__dict__ for ubicacion in ubicaciones]
            for ubicacion_dict in ubicaciones_dicts:
                if '_sa_instance_state' in ubicacion_dict:
                    del ubicacion_dict['_sa_instance_state']
            return jsonify(ubicaciones_dicts)
        else:
            ubicacion = self.control_ubicacion.get(int(id))
            if ubicacion:
                ubicacion_dict = ubicacion.__dict__
                if '_sa_instance_state' in ubicacion_dict:
                    del ubicacion_dict['_sa_instance_state']
                return jsonify(ubicacion_dict)
            abort(404, description="ubicacion no encontrada")
    def post(self):
        ubicacion_data = request.get_json()
        print(ubicacion_data)
        ubicacion = Ubicacion(ubicacion_latitud = ubicacion_data['ubicacion_latitud'], 
                      ubicacion_longitud = ubicacion_data['ubicacion_longitud'],
                      conductor_id = ubicacion_data['conductor_id'])
        print(ubicacion)
        self.control_ubicacion.create(ubicacion)
        return {'resultado': 'ubicacion añadida correctamente'}    
    
    def put(self, id):
        ubicacion_data = request.get_json()
        ubicacion = self.control_ubicacion.get(id)
        if not ubicacion:
            abort(404, message="mina no encontrada")

        if 'ubicacion_latitud' in ubicacion_data:
            ubicacion.ubicacion_latitud = ubicacion_data['ubicacion_latitud']
        if 'ubicacion_longitud' in ubicacion_data:
            ubicacion.ubicacion_longitud = ubicacion_data['ubicacion_longitud']
        if 'conductor_id' in ubicacion_data:
            ubicacion.conductor_id = ubicacion_data['conductor_id']

        self.control_ubicacion.update(ubicacion)
        return jsonify({'resultado': 'ubicacion modificada correctamente'})

    def delete(self, id):
        ubicacion = self.control_ubicacion.get(id)
        if not ubicacion:
            abort(404, message="ubicacion no encontrada")
        self.control_ubicacion.delete(ubicacion)
        return jsonify({'resultado': 'ubicacion borrada correctamente'})