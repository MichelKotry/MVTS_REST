from sqlalchemy.exc import SQLAlchemyError
from conexionBD.Database import Database
from models.Conductor import Conductor
from typing import List
from DAO.IDAO import IDAO


class ConductorDAO(IDAO):
    def __init__(self):
        self.session = Database().SessionLocal()

    def create(self, conductor: Conductor) -> Conductor:
        try:
            self.session.add(conductor)
            self.session.commit()
            self.session.refresh(conductor)
            return conductor
        except SQLAlchemyError as e:
            self.session.rollback()
            raise e

    def get_all(self) -> List[Conductor]:
        try:
            return self.session.query(Conductor).all()
        except SQLAlchemyError as e:
            self.session.rollback()
            raise e
        
    def get(self, conductor_id: int) -> Conductor:
        try:
            return self.session.query(Conductor).filter_by(id=conductor_id).first()
        except SQLAlchemyError as e:
            self.session.rollback()
            raise e

    def update(self, conductor: Conductor) -> Conductor:
        try:
            self.session.commit()
            self.session.refresh(conductor)
            return conductor
        except SQLAlchemyError as e:
            self.session.rollback()
            raise e

    def delete(self, conductor: Conductor):
        try:
            self.session.delete(conductor)
            self.session.commit()
        except SQLAlchemyError as e:
            self.session.rollback()
            raise e
