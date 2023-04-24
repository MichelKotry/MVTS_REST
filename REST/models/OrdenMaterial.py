from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, Numeric
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class OrdenMaterial(Base):
    __tablename__ = 'ordenes_materiales'

    id = Column(Integer, primary_key=True)
    cantidad = Column(Integer, nullable=False)
    orden_id = Column(Integer)
    material_id = Column(Integer)
