from sqlalchemy import Column, Integer, Float, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()

class Ubicacion(Base):
    __tablename__ = 'ubicaciones'

    ubicacion_id = Column(Integer, primary_key=True)
    ubicacion_latitud = Column(Float)
    ubicacion_longitud = Column(Float)
    conductor_id = Column(Integer, ForeignKey('conductores.conductor_id', ondelete='CASCADE'))
    conductor = relationship("Conductor", back_populates="ubicaciones")