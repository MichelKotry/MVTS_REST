from DAO.SemaforoDAO import SemaforoDAO
from models.Semaforo import Semaforo
from controles.IControl import IControl

class ControlSemaforo(IControl):
    def __init__(self):
        self.semaforo_dao = SemaforoDAO()

    def get(self, id):
        return self.semaforo_dao.get(id)

    def get_all(self):
        return self.semaforo_dao.get_all()

    def create(self, semaforo: Semaforo):
        return self.semaforo_dao.create(semaforo)

    def update(self, semaforo: Semaforo):
        return self.semaforo_dao.update(semaforo)

    def delete(self, semaforo: Semaforo):
        return self.semaforo_dao.delete(semaforo)
