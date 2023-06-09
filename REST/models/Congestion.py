from sqlalchemy import Column, Integer, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Congestion(Base):
    __tablename__ = 'congestiones'

    id = Column(Integer, primary_key=True, autoincrement=True)
    fecha_hora = Column(DateTime)
    duracion = Column(Integer)
    ubicacion_id = Column(Integer)
    semaforo_id = Column(Integer)

    