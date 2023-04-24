from flask import jsonify, request,abort
from flask_restful import Resource
from models  import Congestion
from controls import ControlCongestion

class REST_Congestion(Resource):
    def __init__(self):
        self.control_congestion = ControlCongestion()
            
    def get(self, id=None):
        if id is None:
            congestiones = self.control_congestion.get_all()
            congestiones_dicts = [congestion.__dict__ for congestion in congestiones]
            for congestion_dict in congestiones_dicts:
                if '_sa_instance_state' in congestion_dict:
                    del congestion_dict['_sa_instance_state']
            return jsonify(congestiones_dicts)
        else:
            congestion = self.control_congestion.get(int(id))
            if congestion:
                congestion_dict = congestion.__dict__
                if '_sa_instance_state' in congestion_dict:
                    del congestion_dict['_sa_instance_state']
                return jsonify(congestion_dict)
            abort(404, description="Congestion no encontrada")

   
   
    def post(self):
        congestion_data = request.get_json()
        print(congestion_data)
        congestion = Congestion(fecha_hora=congestion_data['fecha_hora'], 
                      duracion=congestion_data['duracion'], 
                      ubicacion_id=congestion_data['ubicacion_id'], 
                      semaforo_id=congestion_data['semaforo_id'])
        print(congestion)
        self.control_congestion.create(congestion)
        return jsonify({'resultado': 'congestion añadida correctamente'})
    
    def put(self, id):
        congestion_data = request.get_json()
        congestion = self.control_congestion.get(id)
        if not congestion:
            abort(404, message="congestion no encontrada")

        if 'fecha_hora' in congestion_data:
            congestion.fecha_hora = congestion_data['fecha_hora']
        if 'duracion' in congestion_data:
            congestion.duracion = congestion_data['duracion']
        if 'ubicacion_id' in congestion_data:
            congestion.ubicacion_id = congestion_data['ubicacion_id']
        if 'semaforo_id' in congestion_data:
            congestion.semaforo_id = congestion_data['semaforo_id']

        self.control_congestion.update(congestion)
        return jsonify({'resultado': 'congestion modificada correctamente'})

    def delete(self, id):
        congestion = self.control_congestion.get(id)
        if not Congestion:
            abort(404, message="congestion no encontrada")
        self.control_congestion.delete(congestion)
        return jsonify({'resultado': 'congestion borrado correctamente'})