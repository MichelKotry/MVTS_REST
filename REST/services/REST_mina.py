from flask import Flask, jsonify, request,abort
from flask_restful import Resource, Api
from models import Mina
from controls import ControlMina

class REST_Mina(Resource):
    def __init__(self):
        self.control_mina = ControlMina()
            
    def get(self, id=None):
        if id is None:
            minas = self.control_mina.get_all()
            mina_dicts = [mina.__dict__ for mina in minas]
            for mina_dict in mina_dicts:
                if '_sa_instance_state' in mina_dict:
                    del mina_dict['_sa_instance_state']
            return jsonify(mina_dicts)
        else:
            mina = self.control_mina.get(int(id))
            if mina:
                mina_dict = mina.__dict__
                if '_sa_instance_state' in mina_dict:
                    del mina_dict['_sa_instance_state']
                return jsonify(mina_dict)
            abort(404, description="mina no encontrada")

    def post(self):
        mina_data = request.get_json()
        print(mina_data)
        mina = Mina(nombre = mina_data['nombre'], 
                      ubicacion_latitud = mina_data['ubicacion_latitud'], 
                      ubicacion_longitud = mina_data['ubicacion_longitud'])
        print(mina)
        self.control_mina.create(mina)
        return {'resultado': 'mina añadida correctamente'}    
    
    def put(self, id):
        mina_data = request.get_json()
        mina = self.control_mina.get(id)
        if not mina:
            abort(404, message="mina no encontrada")

        if 'nombre' in mina_data:
            mina.nombre = mina['nombre']
        if 'ubicacion_latitud' in mina_data:
            mina.ubicacion_latitud = mina_data['ubicacion_latitud']
        if 'ubicacion_longitud' in mina_data:
            mina.ubicacion_longitud = mina_data['ubicacion_longitud']
        
        self.control_conductor.update(mina)
        return jsonify({'resultado': 'mina modificada correctamente'})

    def delete(self, id):
        mina = self.control_mina.get(id)
        if not mina:
            abort(404, message="mina no encontrada")
        self.control_mina.delete(mina)
        return jsonify({'resultado': 'conductor borrado correctamente'})