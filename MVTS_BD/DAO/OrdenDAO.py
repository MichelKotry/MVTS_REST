from sqlalchemy.exc import SQLAlchemyError
from conexionBD.Database import Database
from models.Orden import Orden
from typing import List
from DAO.IDAO import IDAO


class OrdenDAO(IDAO):
    def __init__(self):
        self.session = Database().SessionLocal()

    def create(self, orden: Orden) -> Orden:
        try:
            self.session.add(orden)
            self.session.commit()
            self.session.refresh(orden)
            return orden
        except SQLAlchemyError as e:
            self.session.rollback()
            raise e

    def get_all(self) -> List[Orden]:
        try:
            return self.session.query(Orden).all()
        except SQLAlchemyError as e:
            self.session.rollback()
            raise e
        
    def get(self, orden_id: int) -> Orden:
        try:
            return self.session.query(Orden).filter_by(orden_id=orden_id).first()
        except SQLAlchemyError as e:
            self.session.rollback()
            raise e

    def update(self, orden: Orden) -> Orden:
        try:
            self.session.commit()
            self.session.refresh(orden)
            return orden
        except SQLAlchemyError as e:
            self.session.rollback()
            raise e

    def delete(self, orden: Orden):
        try:
            self.session.delete(orden)
            self.session.commit()
        except SQLAlchemyError as e:
            self.session.rollback()
            raise e
