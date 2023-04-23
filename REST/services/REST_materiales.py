from flask import Flask, jsonify, request,abort
from flask_restful import Resource, Api
from models.models import Material
from controls import ControlMaterial

class REST_Materiales(Resource):
    def __init__(self):
        self.control_material = ControlMaterial()
            
    def get(self, id=None):
        if id is None:
            materiales = self.control_material.get_all()
            materiales_dicts = [material.__dict__ for material in materiales]
            for material_dict in materiales_dicts:
                if '_sa_instance_state' in material_dict:
                    del material_dict['_sa_instance_state']
            return jsonify(materiales_dicts)
        else:
            material = self.control_material.get(int(id))
            if material:
                material_dict = material.__dict__
                if '_sa_instance_state' in material_dict:
                    del material_dict['_sa_instance_state']
                return jsonify(material_dict)
            abort(404, description="material no encontrado")
    
    def post(self):
        material_data = request.get_json()
        print(material_data)
        material = Material(nombre=material_data['nombre'], 
                      tipo_material=material_data['tipo_material'])
        print(material)
        self.control_material.create(material)
        return {'resultado': 'material añadido correctamente'}
    
    def put(self, id):
        material_data = request.get_json()
        material = self.control_material.get(id)
        if not material:
            abort(404, message="material no encontrado")

        if 'nombre' in material_data:
            material.nombre = material_data['nombre']
        if 'tipo_material' in material_data:
            material.tipo_material = material_data['tipo_material']
        

        self.control_material.update(material)
        return jsonify({'resultado': 'material modificado correctamente'})

    def delete(self, id):
        material = self.control_material.get(id)
        if not material:
            abort(404, message="Material no encontrado")
        self.control_material.delete(material)
        return jsonify({'resultado': 'material borrado correctamente'})
    
    