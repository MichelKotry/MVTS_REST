from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, Numeric
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Orden(Base):
    __tablename__ = 'ordenes'

    id = Column(Integer, primary_key=True, autoincrement=True)
    fecha_hora = Column(DateTime)
    estado = Column(String(50))
    gerente_id = Column(Integer)
    vehiculo_id = Column(Integer)
   