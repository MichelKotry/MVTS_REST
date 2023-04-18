from DAO.OrdenDAO import OrdenDAO
from models.Orden import Orden
from controles.IControl import IControl

class ControlOrden(IControl):
    def __init__(self):
        self.orden_dao = OrdenDAO()

    def get(self, id):
        return self.orden_dao.get(id)

    def get_all(self):
        return self.orden_dao.get_all()

    def create(self, orden: Orden):
        return self.orden_dao.create(orden)

    def update(self, orden: Orden):
        return self.orden_dao.update(orden)

    def delete(self, orden: Orden):
        return self.orden_dao.delete(orden)
