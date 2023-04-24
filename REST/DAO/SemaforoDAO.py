from sqlalchemy.exc import SQLAlchemyError
from conexionBD.Database import Database
from models.Semaforo import Semaforo
from typing import List
from DAO.IDAO import IDAO


class SemaforoDAO(IDAO):
    def __init__(self):
        self.session = Database().SessionLocal()

    def create(self, semaforo: Semaforo) -> Semaforo:
        try:
            self.session.add(semaforo)
            self.session.commit()
            self.session.refresh(semaforo)
            return semaforo
        except SQLAlchemyError as e:
            self.session.rollback()
            raise e

    def get_all(self) -> List[Semaforo]:
        try:
            return self.session.query(Semaforo).all()
        except SQLAlchemyError as e:
            self.session.rollback()
            raise e
        
    def get(self, id: int) -> Semaforo:
        try:
            return self.session.query(Semaforo).filter_by(id= id).first()
        except SQLAlchemyError as e:
            self.session.rollback()
            raise e

    def update(self, semaforo: Semaforo) -> Semaforo:
        try:
            self.session.commit()
            self.session.refresh(semaforo)
            return semaforo
        except SQLAlchemyError as e:
            self.session.rollback()
            raise e

    def delete(self, semaforo: Semaforo):
        try:
            self.session.delete(semaforo)
            self.session.commit()
        except SQLAlchemyError as e:
            self.session.rollback()
            raise e
