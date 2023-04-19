from typing import List
from sqlalchemy.exc import SQLAlchemyError
from conexionBD.Database import Database
from models.OrdenMaterial import OrdenMaterial
from DAO.IDAO import IDAO


class OrdenMaterialDAO(IDAO):
    def __init__(self):
        self.session = Database().SessionLocal()

    def create(self, orden_material: OrdenMaterial) -> OrdenMaterial:
        try:
            self.session.add(orden_material)
            self.session.commit()
            self.session.refresh(orden_material)
            return orden_material
        except SQLAlchemyError as e:
            self.session.rollback()
            raise e

    def get_all(self) -> List[OrdenMaterial]:
        try:
            return self.session.query(OrdenMaterial).all()
        except SQLAlchemyError as e:
            self.session.rollback()
            raise e

    def get(self, orden_material_id: int) -> OrdenMaterial:
        try:
            return self.session.query(OrdenMaterial).filter_by(id=orden_material_id).first()
        except SQLAlchemyError as e:
            self.session.rollback()
            raise e

    def update(self, orden_material: OrdenMaterial) -> OrdenMaterial:
        try:
            self.session.commit()
            self.session.refresh(orden_material)
            return orden_material
        except SQLAlchemyError as e:
            self.session.rollback()
            raise e

    def delete(self, orden_material: OrdenMaterial):
        try:
            self.session.delete(orden_material)
            self.session.commit()
        except SQLAlchemyError as e:
            self.session.rollback()
            raise e
