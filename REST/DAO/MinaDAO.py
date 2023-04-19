from sqlalchemy.exc import SQLAlchemyError
from typing import List
from DAO.IDAO import IDAO
from models.Mina import Mina
from conexionBD.Database import Database

class MinaDAO(IDAO):
    def __init__(self):
        self.session = Database().SessionLocal()

    def create(self, mina: Mina) -> Mina:
        try:
            self.session.add(mina)
            self.session.commit()
            self.session.refresh(mina)
            return mina
        except SQLAlchemyError as e:
            self.session.rollback()
            raise e

    def get_all(self) -> List[Mina]:
        try:
            return self.session.query(Mina).all()
        except SQLAlchemyError as e:
            self.session.rollback()
            raise e
        
    def get(self, mina_id: int) -> Mina:
        try:
            return self.session.query(Mina).filter_by(mina_id=mina_id).first()
        except SQLAlchemyError as e:
            self.session.rollback()
            raise e

    def update(self, mina: Mina) -> Mina:
        try:
            self.session.commit()
            self.session.refresh(mina)
            return mina
        except SQLAlchemyError as e:
            self.session.rollback()
            raise e

    def delete(self, mina: Mina):
        try:
            self.session.delete(mina)
            self.session.commit()
        except SQLAlchemyError as e:
            self.session.rollback()
            raise e
