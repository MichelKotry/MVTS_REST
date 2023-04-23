from flask import jsonify, request,abort
from flask_restful import Resource
from models import Orden
from controls import ControlOrden

class REST_Ordenes(Resource):
    def __init__(self):
        self.control_orden = ControlOrden()
            
    def get(self, id=None):
        if id is None:
            ordenes = self.control_orden.get_all()
            ordenes_dicts = [orden.__dict__ for orden in ordenes]
            for orden_dict in ordenes_dicts:
                if '_sa_instance_state' in orden_dict:
                    del orden_dict['_sa_instance_state']
            return jsonify(ordenes_dicts)
        else:
            orden = self.control_orden.get(int(id))
            if orden:
                orden_dict = orden.__dict__
                if '_sa_instance_state' in orden_dict:
                    del orden_dict['_sa_instance_state']
                return jsonify(orden_dict)
            abort(404, description="orden no encontrada")

    def post(self):
        orden_data = request.get_json()
        print(orden_data)
        orden = Orden(fecha_hora = orden_data['fecha_hora'], 
                        estado = orden_data['estado'], 
                        gerente_id = orden_data['gerente_id'],
                        gerente = orden_data['gerente'],
                        vehiculo_id = orden_data['vehiculo_id'],
                        vehiculo = orden_data['vehiculo'])
        print(orden)
        self.control_orden.create(orden)
        return {'resultado': 'orden añadida correctamente'}   
    
    def put(self, id):
        orden_data = request.get_json()
        orden = self.control_orden.get(id)
        if not orden:
            abort(404, message="orden no encontrada")

        if 'fecha_hora' in orden_data:
            orden.fecha_hora = orden['fecha_hora']
        if 'estado' in orden_data:
            orden.estado = orden_data['estado']
        if 'gerente_id' in orden_data:
            orden.gerente_id = orden_data['gerente_id']
        if 'gerente' in orden_data:
            orden.gerente = orden_data['gerente']
        if 'vehiculo_id' in orden_data:
            orden.vehiculo_id = orden_data['vehiculo_id']
        if 'vehiculo' in orden_data:
            orden.vehiculo = orden_data['vehiculo']


        self.control_orden.update(orden)
        return jsonify({'resultado': 'orden modificada correctamente'})

    def delete(self, id):
        orden = self.control_orden.get(id)
        if not orden:
            abort(404, message="orden no encontrada")
        self.control_orden.delete(orden)
        return jsonify({'resultado': 'orden borrada correctamente'})
    
        