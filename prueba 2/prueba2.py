from flask import Flask, jsonify, request,abort
from flask_restful import Resource, Api
from conductor import Conductor
from vehiculo import Vehiculo
from mina import Mina
from gerentes import Gerentes
from materiales import Materiales
from ordenes import Ordenes
from semaforos import Semaforo
from ubicaciones import Ubicaciones
from congestiones import Congestiones
from ordenesMateriales import OrdenesMateriales

app = Flask(__name__)
api = Api(app)

#Asignamos las Direcciones   
api.add_resource(Gerentes, '/gernte/<string:valor>', '/gerente/')
api.add_resource(Conductor, '/conductor/<string:valor>', '/conductor/')
api.add_resource(Vehiculo, '/vehiculo/<string:valor>', '/vehiculo/')
api.add_resource(Mina, '/mina/<string:valor>', '/mina/')
api.add_resource(Materiales, '/materiales/<string:valor>', '/materiales/')
api.add_resource(Ordenes, '/ordenes/<string:valor>', '/ordenes/')
api.add_resource(Semaforo, '/semaforo/<string:valor>', '/semaforo/')
api.add_resource(Ubicaciones, '/ubicaciones/<string:valor>', '/ubicaciones/')
api.add_resource(Congestiones, '/congestiones/<string:valor>', '/congestiones/')
api.add_resource(OrdenesMateriales, '/ordenMaterial/<string:valor>', '/ordenMaterial/')

if __name__ == '__main__':
    app.run(debug=True)
    