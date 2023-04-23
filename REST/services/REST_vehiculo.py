from flask import Flask, jsonify, request,abort
from flask_restful import Resource, Api
from models import Vehiculo
from controls import ControlVehiculo

class REST_Vehiculo(Resource):
    def __init__(self):
        self.control_vehiculo = ControlVehiculo()
            
    def get(self, id=None):
        if id is None:
            vehiculos = self.control_vehiculo.get_all()
            vehiculos_dicts = [vehiculo.__dict__ for vehiculo in vehiculos]
            for vehiculo_dict in vehiculos_dicts:
                if '_sa_instance_state' in vehiculo_dict:
                    del vehiculo_dict['_sa_instance_state']
            return jsonify(vehiculos_dicts)
        else:
            vehiculo = self.control_vehiculo.get(int(id))
            if vehiculo:
                vehiculo_dict = vehiculo.__dict__
                if '_sa_instance_state' in vehiculo_dict:
                    del vehiculo_dict['_sa_instance_state']
                return jsonify(vehiculo_dict)
            abort(404, description="vehiculo no encontrado")



    def post(self):
        vehiculo_data = request.get_json()
        print(vehiculo_data)
        vehiculo = Vehiculo(modelo=vehiculo_data['modelo'], 
                      placa=vehiculo_data['placa'], 
                      ubicacion_latitud=vehiculo_data['ubicacion_latitud'],
                      ubicacion_longitud=vehiculo_data['ubicacion_longitud'], 
                      estado=vehiculo_data['estado'], 
                      conductor_id=vehiculo_data['conductor_id'],  
                      mina_id=vehiculo_data['mina_id'])
        print(vehiculo)
        self.control_vehiculo.create(vehiculo)
        return {'resultado': 'vehiculo añadido correctamente'}
    
    def put(self, id):
        vehiculo_data = request.get_json()
        vehiculo = self.control_vehiculo.get(id)
        if not vehiculo:
            abort(404, message="vehiculo no encontrado")

        if 'modelo' in vehiculo_data:
            vehiculo.modelo = vehiculo_data['modelo']
        if 'placa' in vehiculo_data:
            vehiculo.placa = vehiculo_data['placa']
        if 'ubicacion_latitud' in vehiculo_data:
            vehiculo.ubicacion_latitud = vehiculo_data['ubicacion_latitud']
        if 'ubicacion_longitud' in vehiculo_data:
            vehiculo.ubicacion_longitud = vehiculo_data['ubicacion_longitud']
        if 'estado' in vehiculo_data:
            vehiculo.estado = vehiculo_data['estado']
        if 'conductor_id' in vehiculo_data:
            vehiculo.conductor_id = vehiculo_data['conductor_id']
        if 'mina_id' in vehiculo_data:
            vehiculo.mina_id = vehiculo_data['mina_id']
        
#
        self.control_vehiculo.update(vehiculo)
        return jsonify({'resultado': 'vehiculo modificado correctamente'})

    def delete(self, id):
        vehiculo = self.control_vehiculo.get(id)
        if not vehiculo:
            abort(404, message="Vehiculo no encontrado")
        self.control_vehiculo.delete(vehiculo)
        return jsonify({'resultado': 'vehiculo borrado correctamente'})
  
