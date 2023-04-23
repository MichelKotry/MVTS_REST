from sqlalchemy import Column, Integer, String, ForeignKey, Float
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from models import Conductor
Base = declarative_base()

class Vehiculo(Base):
    __tablename__ = 'vehiculos'

    id = Column(Integer, primary_key=True, autoincrement=True)
    modelo = Column(String(255))
    placa = Column(String(20))
    ubicacion_latitud = Column(Float)
    ubicacion_longitud = Column(Float)
    estado = Column(String(50))
    conductor_id = Column(Integer, ForeignKey('conductores.id', ondelete='CASCADE'))
    conductor = relationship('Conductor', backref='vehiculos') 
    mina_id = Column(Integer, ForeignKey('minas.id', ondelete='CASCADE'))
    mina = relationship('Mina', backref='vehiculos')
