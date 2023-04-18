from DAO.UbicacionDAO import UbicacionDAO
from models.Ubicacion import Ubicacion
from controles.IControl import IControl

class ControlUbicacion(IControl):
    def __init__(self):
        self.ubicacion_dao = UbicacionDAO()

    def get(self, id):
        return self.ubicacion_dao.get(id)

    def get_all(self):
        return self.ubicacion_dao.get_all()

    def create(self, ubicacion: Ubicacion):
        return self.ubicacion_dao.create(ubicacion)

    def update(self, ubicacion: Ubicacion):
        return self.ubicacion_dao.update(ubicacion)

    def delete(self, ubicacion: Ubicacion):
        return self.ubicacion_dao.delete(ubicacion)
