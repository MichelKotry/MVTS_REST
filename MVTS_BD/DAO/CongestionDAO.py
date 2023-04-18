from sqlalchemy.exc import SQLAlchemyError
from conexionBD.Database import Database
from models.Congestion import Congestion
from typing import List
from DAO.IDAO import IDAO


class CongestionDAO(IDAO):
    def __init__(self):
        self.session = Database().SessionLocal()

    def create(self, congestion: Congestion) -> Congestion:
        try:
            self.session.add(congestion)
            self.session.commit()
            self.session.refresh(congestion)
            return congestion
        except SQLAlchemyError as e:
            self.session.rollback()
            raise e

    def get_all(self) -> List[Congestion]:
        try:
            return self.session.query(Congestion).all()
        except SQLAlchemyError as e:
            self.session.rollback()
            raise e
        
    def get(self, congestion_id: int) -> Congestion:
        try:
            return self.session.query(Congestion).filter_by(congestion_id=congestion_id).first()
        except SQLAlchemyError as e:
            self.session.rollback()
            raise e

    def update(self, congestion: Congestion) -> Congestion:
        try:
            self.session.commit()
            self.session.refresh(congestion)
            return congestion
        except SQLAlchemyError as e:
            self.session.rollback()
            raise e

    def delete(self, congestion: Congestion):
        try:
            self.session.delete(congestion)
            self.session.commit()
        except SQLAlchemyError as e:
            self.session.rollback()
            raise e
