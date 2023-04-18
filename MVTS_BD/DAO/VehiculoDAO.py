from typing import List
from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError
from models.Vehiculo import Vehiculo
from DAO.IDAO import IDAO
from conexionBD.Database import Database

class VehiculoDAO(IDAO):
    def __init__(self):
        self.session = Database().SessionLocal()

    def create(self, vehiculo: Vehiculo) -> Vehiculo:
        try:
            self.session.add(vehiculo)
            self.session.commit()
            self.session.refresh(vehiculo)
            return vehiculo
        except SQLAlchemyError as e:
            self.session.rollback()
            raise e

    def get_all(self) -> List[Vehiculo]:
        try:
            return self.session.query(Vehiculo).all()
        except SQLAlchemyError as e:
            self.session.rollback()
            raise e

    def get(self, vehiculo_id: int) -> Vehiculo:
        try:
            return self.session.query(Vehiculo).filter_by(vehiculo_id=vehiculo_id).first()
        except SQLAlchemyError as e:
            self.session.rollback()
            raise e

    def update(self, vehiculo: Vehiculo) -> Vehiculo:
        try:
            self.session.commit()
            self.session.refresh(vehiculo)
            return vehiculo
        except SQLAlchemyError as e:
            self.session.rollback()
            raise e

    def delete(self, vehiculo: Vehiculo):
        try:
            self.session.delete(vehiculo)
            self.session.commit()
        except SQLAlchemyError as e:
            self.session.rollback()
            raise e
