from flask import Flask, jsonify, request,abort
from flask_restful import Resource, Api
from models.models import Gerente
from controls import ControlGerente
personas_lista = []

class REST_Gerentes(Resource):
    def __init__(self):
        self.control_gerente = ControlGerente()
            
    def get(self, id=None):
        if id is None:
            gerentes = self.control_gerente.get_all()
            gerentes_dicts = [gerente.__dict__ for gerente in gerentes]
            for gerente_dict in gerentes_dicts:
                if '_sa_instance_state' in gerente_dict:
                    del gerente_dict['_sa_instance_state']
            return jsonify(gerentes_dicts)
        else:
            gerente = self.control_gerente.get(int(id))
            if gerente:
                gerente_dict = gerente.__dict__
                if '_sa_instance_state' in gerente_dict:
                    del gerente_dict['_sa_instance_state']
                return jsonify(gerente_dict)
            abort(404, description="grente no encontrado")

    def post(self):
        gerente_data = request.get_json()
        print(gerente_data)
        gerente = Gerente(nombre = gerente_data['nombre'], 
                      correo_electronico = gerente_data['correo_electronico'], 
                      fecha_nacimiento = gerente_data['fecha_nacimiento'],
                      telefono = gerente_data['telefono'])
        print(gerente)
        self.control_gerente.create(gerente)
        return {'resultado': 'gerente añadido correctamente'}    
    
    def put(self, id):
        gerente_data = request.get_json()
        gerente = self.control_gerente.get(id)
        if not gerente:
            abort(404, message="gerente no encontrada")

        if 'nombre' in gerente_data:
            gerente.nombre = gerente['nombre']
        if 'correo_electronico' in gerente_data:
            gerente.correo_electronico = gerente_data['correo_electronico']
        if 'fecha_nacimiento' in gerente_data:
            gerente.fecha_nacimiento = gerente_data['fecha_nacimiento']
        if 'telefono' in gerente_data:
            gerente.telefono = gerente_data['telefono']
        
        self.control_gerente.update(gerente)
        return jsonify({'resultado': 'gerente modificado correctamente'})

    def delete(self, id):
        gerente = self.control_gerente.get(id)
        if not gerente:
            abort(404, message="gerente no encontrada")
        self.control_gerente.delete(gerente)
        return jsonify({'resultado': 'gerente borrado correctamente'})

