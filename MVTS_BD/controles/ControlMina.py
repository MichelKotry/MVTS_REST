from DAO.MinaDAO import MinaDAO
from models.Mina import Mina
from controles.IControl import IControl

class ControlMina(IControl):
    def __init__(self):
        self.mina_dao = MinaDAO()

    def get(self, id):
        return self.mina_dao.get(id)

    def get_all(self):
        return self.mina_dao.get_all()

    def create(self, mina: Mina):
        return self.mina_dao.create(mina)

    def update(self, mina: Mina):
        return self.mina_dao.update(mina)

    def delete(self, mina: Mina):
        return self.mina_dao.delete(mina)
