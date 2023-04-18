from DAO.VehiculoDAO import VehiculoDAO
from models.Vehiculo import Vehiculo
from controles.IControl import IControl

class ControlVehiculo(IControl):
    def __init__(self):
        self.vehiculo_dao = VehiculoDAO()

    def get(self, id):
        return self.vehiculo_dao.get(id)

    def get_all(self):
        return self.vehiculo_dao.get_all()

    def create(self, vehiculo: Vehiculo):
        return self.vehiculo_dao.create(vehiculo)

    def update(self, vehiculo: Vehiculo):
        return self.vehiculo_dao.update(vehiculo)

    def delete(self, vehiculo: Vehiculo):
        return self.vehiculo_dao.delete(vehiculo)