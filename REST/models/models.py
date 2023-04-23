from sqlalchemy import Column, Integer, String, DateTime, Float, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()


class Conductor(Base):
    __tablename__ = 'conductores'
    id = Column(Integer, primary_key=True)
    nombre = Column(String(255))
    correo_electronico = Column(String(255))
    fecha_nacimiento = Column(DateTime)
    telefono = Column(String(20))

    vehiculos = relationship("Vehiculo", back_populates="conductor")

class Gerente(Base):
    __tablename__ = 'gerentes'

    id = Column(Integer, primary_key=True)
    nombre = Column(String(255))
    correo_electronico = Column(String(255))
    fecha_nacimiento = Column(DateTime)
    telefono = Column(String(20))

class Mina(Base):
    __tablename__ = 'minas'
    id = Column(Integer, primary_key=True)
    nombre = Column(String(255))
    ubicacion_latitud = Column(Float)
    ubicacion_longitud = Column(Float)
    
    vehiculos = relationship("Vehiculo", back_populates="mina")

class Vehiculo(Base):
    __tablename__ = 'vehiculos'
    id = Column(Integer, primary_key=True)
    modelo = Column(String(255))
    placa = Column(String(20))
    ubicacion_latitud = Column(Float)
    ubicacion_longitud = Column(Float)
    estado = Column(String(50))
    
    conductor_id = Column(Integer, ForeignKey('conductores.id', ondelete='CASCADE'))
    conductor = relationship("Conductor", back_populates="vehiculos")
    
    mina_id = Column(Integer, ForeignKey('minas.id', ondelete='CASCADE'))
    mina = relationship("Mina", back_populates="vehiculos")

class Orden(Base):
    __tablename__ = 'ordenes'

    id = Column(Integer, primary_key=True, autoincrement=True)
    fecha_hora = Column(DateTime)
    estado = Column(String(50))
    gerente_id = Column(Integer, ForeignKey('gerentes.id', ondelete='CASCADE'))
    vehiculo_id = Column(Integer, ForeignKey('vehiculos.id', ondelete='CASCADE'))
    gerente = relationship("Gerente")
    vehiculo = relationship("Vehiculo")

class Material(Base):
    __tablename__ = 'materiales'

    id = Column(Integer, primary_key=True)
    nombre = Column(String(255))
    tipo_material = Column(String(50))

class OrdenMaterial(Base):
    __tablename__ = 'ordenes_materiales'

    id = Column('orden_material_id', Integer, primary_key=True)
    cantidad = Column(Integer, nullable=False)

    orden_id = Column(Integer, ForeignKey('ordenes.id', ondelete='CASCADE'))
    material_id = Column(Integer, ForeignKey('materiales.id', ondelete='CASCADE'))

    orden = relationship('Orden', back_populates='materiales')
    material = relationship('Material')

class Ubicacion(Base):
    __tablename__ = 'ubicaciones'

    id = Column(Integer, primary_key=True)
    ubicacion_latitud = Column(Float)
    ubicacion_longitud = Column(Float)
    conductor_id = Column(Integer, ForeignKey('conductores.id', ondelete='CASCADE'))
    conductor = relationship("Conductor", back_populates="ubicaciones")

class Semaforo(Base):
    __tablename__ = 'semaforo'

    id = Column(Integer, primary_key=True)
    fecha_hora = Column(DateTime)
    duracion = Column(Integer)
    ubicacion_id = Column(Integer, ForeignKey('ubicaciones.id', ondelete='CASCADE'))
    ubicacion = relationship("Ubicacion")
    semaforo_id = Column(Integer, ForeignKey('semaforos.id', ondelete='CASCADE'))
    semaforo = relationship("Semaforo")

class Congestion(Base):
    __tablename__ = 'congestiones'

    id = Column(Integer, primary_key=True, autoincrement=True)
    fecha_hora = Column(DateTime)
    duracion = Column(Integer)
    ubicacion_id = Column(Integer, ForeignKey('ubicaciones.id', ondelete='CASCADE'))
    semaforo_id = Column(Integer, ForeignKey('semaforos.id', ondelete='CASCADE'))

    ubicacion = relationship("Ubicacion", back_populates="congestiones")
    semaforo = relationship("Semaforo", back_populates="congestiones")