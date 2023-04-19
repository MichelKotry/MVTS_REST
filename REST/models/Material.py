from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Material(Base):
    __tablename__ = 'materiales'

    id = Column(Integer, primary_key=True)
    nombre = Column(String(255))
    tipo_material = Column(String(50))