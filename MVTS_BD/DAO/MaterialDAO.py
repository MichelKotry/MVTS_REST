from typing import List
from sqlalchemy.exc import SQLAlchemyError
from conexionBD.Database import Database
from models.Material import Material
from DAO.IDAO import IDAO


class MaterialDAO(IDAO):
    def __init__(self):
        self.session = Database().SessionLocal()

    def create(self, material: Material) -> Material:
        try:
            self.session.add(material)
            self.session.commit()
            self.session.refresh(material)
            return material
        except SQLAlchemyError as e:
            self.session.rollback()
            raise e

    def get_all(self) -> List[Material]:
        try:
            return self.session.query(Material).all()
        except SQLAlchemyError as e:
            self.session.rollback()
            raise e
        
    def get(self, material_id: int) -> Material:
        try:
            return self.session.query(Material).filter_by(material_id=material_id).first()
        except SQLAlchemyError as e:
            self.session.rollback()
            raise e

    def update(self, material: Material) -> Material:
        try:
            self.session.commit()
            self.session.refresh(material)
            return material
        except SQLAlchemyError as e:
            self.session.rollback()
            raise e

    def delete(self, material: Material):
        try:
            self.session.delete(material)
            self.session.commit()
        except SQLAlchemyError as e:
            self.session.rollback()
            raise e
