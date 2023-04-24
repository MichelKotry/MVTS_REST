from sqlalchemy import Column, Integer, String, Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()
class Mina(Base):
    __tablename__ = 'minas'
    id = Column(Integer, primary_key=True)
    nombre = Column(String(255))
    ubicacion_latitud = Column(Float)
    ubicacion_longitud = Column(Float)
    
   
