from sqlalchemy.exc import SQLAlchemyError
from conexionBD.Database import Database
from models.Gerente import Gerente
from typing import List
from DAO import IDAO

class GerenteDAO(IDAO):
    def __init__(self):
        self.session = Database().SessionLocal()

    def create(self, gerente: Gerente) -> Gerente:
        try:
            self.session.add(gerente)
            self.session.commit()
            self.session.refresh(gerente)
            return gerente
        except SQLAlchemyError as e:
            self.session.rollback()
            raise e

    def get_all(self) -> List[Gerente]:
        try:
            return self.session.query(Gerente).all()
        except SQLAlchemyError as e:
            self.session.rollback()
            raise e
        
    def get(self, gerente_id: int) -> Gerente:
        try:
            return self.session.query(Gerente).filter_by(id=gerente_id).first()
        except SQLAlchemyError as e:
            self.session.rollback()
            raise e

    def update(self, gerente: Gerente) -> Gerente:
        try:
            self.session.commit()
            self.session.refresh(gerente)
            return gerente
        except SQLAlchemyError as e:
            self.session.rollback()
            raise e

    def delete(self, gerente: Gerente):
        try:
            self.session.delete(gerente)
            self.session.commit()
        except SQLAlchemyError as e:
            self.session.rollback()
            raise e
