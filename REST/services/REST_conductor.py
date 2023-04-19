
from flask import Flask, jsonify, request,abort
from flask_restful import Resource, Api
from models import Conductor
from controls import ControlConductor



class REST_Conductor(Resource):
    def __init__(self):
        self.control_conductor = ControlConductor()
            
    def get(self, id=None):
        if id is None:
            conductores = self.control_conductor.get_all()
            conductores_dicts = [conductor.__dict__ for conductor in conductores]
            for conductor_dict in conductores_dicts:
                if '_sa_instance_state' in conductor_dict:
                    del conductor_dict['_sa_instance_state']
            return jsonify(conductores_dicts)
        else:
            conductor = self.control_conductor.get(int(id))
            if conductor:
                conductor_dict = conductor.__dict__
                if '_sa_instance_state' in conductor_dict:
                    del conductor_dict['_sa_instance_state']
                return jsonify(conductor_dict)
            abort(404, description="Conductor no encontrado")



    def post(self):
        conductor_data = request.get_json()
        print(conductor_data)
        conductor = Conductor(nombre=conductor_data['nombre'], 
                      correo_electronico=conductor_data['correo_electronico'], 
                      fecha_nacimiento=conductor_data['fecha_nacimiento'], 
                      telefono=conductor_data['telefono'])
        print(conductor)
        self.control_conductor.create(conductor)
        return {'resultado': 'conductor añadido correctamente'}
    
    def put(self, id):
        conductor_data = request.get_json()
        conductor = self.control_conductor.get(id)
        if not conductor:
            abort(404, message="Conductor no encontrado")

        if 'nombre' in conductor_data:
            conductor.nombre = conductor_data['nombre']
        if 'correo_electronico' in conductor_data:
            conductor.correo_electronico = conductor_data['correo_electronico']
        if 'fecha_nacimiento' in conductor_data:
            conductor.fecha_nacimiento = conductor_data['fecha_nacimiento']
        if 'telefono' in conductor_data:
            conductor.telefono = conductor_data['telefono']

        self.control_conductor.update(conductor)
        return jsonify({'resultado': 'conductor modificado correctamente'})

    def delete(self, id):
        conductor = self.control_conductor.get(id)
        if not conductor:
            abort(404, message="Conductor no encontrado")
        self.control_conductor.delete(conductor)
        return jsonify({'resultado': 'conductor borrado correctamente'})
