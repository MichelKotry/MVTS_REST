from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Conductor(Base):
    __tablename__ = 'conductores'

    conductor_id = Column(Integer, primary_key=True)
    nombre = Column(String(255))
    correo_electronico = Column(String(255))
    fecha_nacimiento = Column(DateTime)
    telefono = Column(String(20))
