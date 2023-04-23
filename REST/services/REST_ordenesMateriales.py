from flask import  jsonify, request,abort
from flask_restful import Resource
from models.models import OrdenMaterial
from controls import ControlOrdenMaterial

class REST_OrdenesMateriales(Resource):
    def __init__(self):
        self.control_ordenMaterial = ControlOrdenMaterial()
            
    def get(self, id=None):
        if id is None:
            ordenesMaterial = self.control_ordenMaterial.get_all()
            ordenesMaterial_dicts = [ordenMaterial.__dict__ for ordenMaterial  in ordenesMaterial]
            for ordenMaterial_dict in ordenesMaterial_dicts:
                if '_sa_instance_state' in ordenMaterial_dict:
                    del ordenMaterial_dict['_sa_instance_state']
            return jsonify(ordenesMaterial_dicts)
        else:
            ordenMaterial = self.control_ordenMaterial.get(int(id))
            if ordenMaterial:
                ordenMaterial_dict = ordenMaterial.__dict__
                if '_sa_instance_state' in ordenMaterial_dict:
                    del ordenMaterial_dict['_sa_instance_state']
                return jsonify(ordenMaterial_dict)
            abort(404, description="orden no encontrada")

    def post(self):
        ordenMaterial_data = request.get_json()
        print(ordenMaterial_data)
        ordenMaterial = OrdenMaterial(cantidad = ordenMaterial_data['cantidad'], 
                        orden_id = ordenMaterial_data['orden_id'], 
                        material_id = ordenMaterial_data['material_id'])
        
        print(ordenMaterial)
        self.control_orden.create(ordenMaterial)
        return {'resultado': 'orden añadida correctamente'}  
    
    def put(self, id):
        ordenMaterial_data = request.get_json()
        ordenMaterial = self.control_ordenMaterial.get(id)
        if not ordenMaterial:
            abort(404, message="orden no encontrada")

        if 'cantidad' in ordenMaterial_data:
            ordenMaterial.cantidad = ordenMaterial['cantidad']
        if 'orden_id' in ordenMaterial_data:
            ordenMaterial.orden_id = ordenMaterial['orden_id']
        if 'material_id' in ordenMaterial_data:
            ordenMaterial.material_id = ordenMaterial['material_id']
        

        self.control_ordenMaterial.update(ordenMaterial)
        return jsonify({'resultado': 'orden modificada correctamente'})

    def delete(self, id):
        ordenMaterial = self.control_ordenMaterial.get(id)
        if not ordenMaterial:
            abort(404, message="orden no encontrada")
        self.control_ordenMaterial.delete(ordenMaterial)
        return jsonify({'resultado': 'orden borrada correctamente'})
    