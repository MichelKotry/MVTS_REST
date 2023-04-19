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
api.add_resource(REST_Gerentes, '/gernte/<string:valor>', '/gerente/')
api.add_resource(REST_Conductor, '/conductor/<string:id>', '/conductor/')
api.add_resource(REST_Vehiculo, '/vehiculo/<string:valor>', '/vehiculo/')
api.add_resource(REST_Mina, '/mina/<string:valor>', '/mina/')
api.add_resource(REST_Materiales, '/materiales/<string:valor>', '/materiales/')
api.add_resource(REST_Ordenes, '/ordenes/<string:valor>', '/ordenes/')
api.add_resource(REST_Semaforo, '/semaforo/<string:valor>', '/semaforo/')
api.add_resource(REST_Ubicaciones, '/ubicaciones/<string:valor>', '/ubicaciones/')
api.add_resource(REST_Congestion, '/congestiones/<string:valor>', '/congestiones/')
api.add_resource(REST_OrdenesMateriales, '/ordenMaterial/<string:valor>', '/ordenMaterial/')

if __name__ == '__main__':
    app.run(debug=True)
    