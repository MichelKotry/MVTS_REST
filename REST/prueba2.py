from flask import Flask, jsonify, request,abort
from flask_restful import Resource, Api
from services import REST_Conductor
from services import REST_Vehiculo
from services import REST_Mina
from services import REST_Gerentes
from services import REST_Materiales
from services import REST_Ordenes
from services import REST_Semaforo
from services import REST_Ubicaciones
from services import REST_Congestion
from services import REST_OrdenesMateriales

app = Flask(__name__)
api = Api(app)

#Asignamos las Direcciones   
api.add_resource(REST_Gerentes, '/gernte/<int:id>', '/gerente/')
api.add_resource(REST_Conductor, '/conductor/<int:id>', '/conductor/')
api.add_resource(REST_Vehiculo, '/vehiculo/<int:id>' , '/vehiculo/')
api.add_resource(REST_Mina, '/mina/<int:id>', '/mina/')
api.add_resource(REST_Materiales, '/materiales/<int:id>', '/materiales/')
api.add_resource(REST_Ordenes, '/ordenes/<int:id>', '/ordenes/')
api.add_resource(REST_Semaforo, '/semaforo/<int:id>', '/semaforo/')
api.add_resource(REST_Ubicaciones, '/ubicaciones/<int:id>', '/ubicaciones/')
api.add_resource(REST_Congestion, '/congestiones/<int:id>', '/congestiones/')
api.add_resource(REST_OrdenesMateriales, '/ordenMaterial/<int:id>', '/ordenMaterial/')

if __name__ == '__main__':
    app.run(debug=True)
    