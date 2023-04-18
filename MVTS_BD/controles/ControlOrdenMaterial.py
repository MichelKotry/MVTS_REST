from DAO.OrdenMaterialDAO import OrdenMaterialDAO
from models.OrdenMaterial import OrdenMaterial
from controles.IControl import IControl

class ControlOrdenMaterial(IControl):
    def __init__(self):
        self.orden_material_dao = OrdenMaterialDAO()

    def get(self, id):
        return self.orden_material_dao.get(id)

    def get_all(self):
        return self.orden_material_dao.get_all()

    def create(self, orden_material: OrdenMaterial):
        return self.orden_material_dao.create(orden_material)

    def update(self, orden_material: OrdenMaterial):
        return self.orden_material_dao.update(orden_material)

    def delete(self, orden_material: OrdenMaterial):
        return self.orden_material_dao.delete(orden_material)
