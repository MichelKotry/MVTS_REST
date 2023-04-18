from sqlalchemy import Column, Integer, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Congestion(Base):
    __tablename__ = 'congestiones'

    congestion_id = Column(Integer, primary_key=True, autoincrement=True)
    fecha_hora = Column(DateTime)
    duracion = Column(Integer)
    ubicacion_id = Column(Integer, ForeignKey('ubicaciones.ubicacion_id', ondelete='CASCADE'))
    semaforo_id = Column(Integer, ForeignKey('semaforos.semaforo_id', ondelete='CASCADE'))

    ubicacion = relationship("Ubicacion", back_populates="congestiones")
    semaforo = relationship("Semaforo", back_populates="congestiones")