from models.Conductor import Conductor
from DAO.ConductorDAO import ConductorDAO
from controles.ControlConductor import ControlConductor
from datetime import datetime

conductor_dao = ConductorDAO()
control_conductor = ControlConductor()

conductor = Conductor(nombre="Kotry", email="Kotry@gmail.com", fecha_nacimiento=datetime(1990, 1, 1), telefono="63312435")

#conductor_creado = conductor_dao.create(conductor)
conductor_creado = control_conductor.create(conductor)
print(conductor_creado.id)  # El ID del conductor creado

#conductores = conductor_dao.get_all()
conductores = control_conductor.get_all()
print(conductores[0].nombre)  # Lista de todos los conductores

#conductor_obtenido = conductor_dao.get(1)
conductor_obtenido = control_conductor.get(3)
print(conductor_obtenido.email)  # Nombre del conductor obtenido

conductor_obtenido.email = "manuel.corral248399@potros.itson.edu.mx"
#conductor_actualizado = conductor_dao.update(conductor_obtenido)
conductor_actualizado = control_conductor.update(conductor_obtenido)
print(conductor_actualizado.email)  # Edad actualizada del conductor


#conductor_dao.delete(conductor_actualizado)
control_conductor.delete(conductor_actualizado)




