from sqlalchemy import Column, Integer, String, ForeignKey, Float, DateTime
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Semaforo(Base):
    __tablename__ = 'semaforo'

    id = Column(Integer, primary_key=True)
    fecha_hora = Column(DateTime)
    duracion = Column(Integer)
    ubicacion_id = Column(Integer, ForeignKey('ubicaciones.id', ondelete='CASCADE'))
    ubicacion = relationship("Ubicacion")
    semaforo_id = Column(Integer, ForeignKey('semaforos.id', ondelete='CASCADE'))
    semaforo = relationship("Semaforo")