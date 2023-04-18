from DAO.CongestionDAO import CongestionDAO
from models.Congestion import Congestion
from controles.IControl import IControl

class ControlCongestion(IControl):
    def __init__(self):
        self.congestion_dao = CongestionDAO()

    def get(self, id):
        return self.congestion_dao.get(id)

    def get_all(self):
        return self.congestion_dao.get_all()

    def create(self, congestion: Congestion):
        return self.congestion_dao.create(congestion)

    def update(self, congestion: Congestion):
        return self.congestion_dao.update(congestion)

    def delete(self, congestion: Congestion):
        return self.congestion_dao.delete(congestion)
