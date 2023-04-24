from sqlalchemy import Column, Integer, String, ForeignKey, Float, DateTime
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Semaforo(Base):
    __tablename__ = 'semaforos'

    id = Column(Integer, primary_key=True)
    ubicacion_latitud = Column(Float)
    ubicacion_longitud = Column(Float)
    estado = Column(String(50))
    tipo = Column(String(50))
    mina_id = Column(Integer)
