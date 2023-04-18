from DAO.MaterialDAO import MaterialDAO
from models.Material import Material
from controles.IControl import IControl

class ControlMaterial(IControl):
    def __init__(self):
        self.material_dao = MaterialDAO()

    def get(self, id):
        return self.material_dao.get(id)

    def get_all(self):
        return self.material_dao.get_all()

    def create(self, material: Material):
        return self.material_dao.create(material)

    def update(self, material: Material):
        return self.material_dao.update(material)

    def delete(self, material: Material):
        return self.material_dao.delete(material)
