from DAO.GerenteDAO import GerenteDAO
from models.Gerente import Gerente
from controles.IControl import IControl

class ControlGerente(IControl):
    def __init__(self):
        self.gerente_dao = GerenteDAO()

    def get(self, id):
        return self.gerente_dao.get(id)

    def get_all(self):
        return self.gerente_dao.get_all()

    def create(self, gerente: Gerente):
        return self.gerente_dao.create(gerente)

    def update(self, gerente: Gerente):
        return self.gerente_dao.update(gerente)

    def delete(self, gerente: Gerente):
        return self.gerente_dao.delete(gerente)
