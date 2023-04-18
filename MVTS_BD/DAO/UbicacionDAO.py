from typing import List
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.orm import Session
from models.Ubicacion import Ubicacion
from DAO.IDAO import IDAO
from conexionBD.Database import Database

class UbicacionDAO(IDAO):
    def __init__(self):
        self.session: Session = Database().SessionLocal()

    def create(self, ubicacion: Ubicacion) -> Ubicacion:
        try:
            self.session.add(ubicacion)
            self.session.commit()
            self.session.refresh(ubicacion)
            return ubicacion
        except SQLAlchemyError as e:
            self.session.rollback()
            raise e

    def get_all(self) -> List[Ubicacion]:
        try:
            return self.session.query(Ubicacion).all()
        except SQLAlchemyError as e:
            self.session.rollback()
            raise e

    def get(self, ubicacion_id: int) -> Ubicacion:
        try:
            return self.session.query(Ubicacion).filter_by(ubicacion_id=ubicacion_id).first()
        except SQLAlchemyError as e:
            self.session.rollback()
            raise e

    def update(self, ubicacion: Ubicacion) -> Ubicacion:
        try:
            self.session.commit()
            self.session.refresh(ubicacion)
            return ubicacion
        except SQLAlchemyError as e:
            self.session.rollback()
            raise e

    def delete(self, ubicacion: Ubicacion):
        try:
            self.session.delete(ubicacion)
            self.session.commit()
        except SQLAlchemyError as e:
            self.session.rollback()
            raise e
