from DAO.ConductorDAO import ConductorDAO
from models.Conductor import Conductor
from controles.IControl import IControl

class ControlConductor(IControl):
    def __init__(self):
        self.conductor_dao = ConductorDAO()

    def get(self, id):
        return self.conductor_dao.get(id)

    def get_all(self):
        return self.conductor_dao.get_all()

    def create(self, conductor: Conductor):
        return self.conductor_dao.create(conductor)

    def update(self, conductor: Conductor):
        return self.conductor_dao.update(conductor)

    def delete(self, conductor: Conductor):
        return self.conductor_dao.delete(conductor)
