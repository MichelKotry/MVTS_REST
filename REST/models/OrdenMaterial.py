from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, Numeric
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class OrdenMaterial(Base):
    __tablename__ = 'ordenes_materiales'

    id = Column('orden_material_id', Integer, primary_key=True)
    cantidad = Column(Integer, nullable=False)

    orden_id = Column(Integer, ForeignKey('ordenes.orden_id', ondelete='CASCADE'))
    material_id = Column(Integer, ForeignKey('materiales.material_id', ondelete='CASCADE'))

    orden = relationship('Orden', back_populates='materiales')
    material = relationship('Material')