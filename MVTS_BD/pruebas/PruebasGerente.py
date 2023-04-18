from models.Gerente import Gerente
from DAO.GerenteDAO import GerenteDAO
from controles.ControlGerente import ControlGerente
from datetime import datetime

gerente_dao = GerenteDAO()
control_gerente = ControlGerente()

gerente = Gerente(nombre="Kotry", correo_electronico="Kotry@gmail.com", fecha_nacimiento=datetime(1990, 1, 1), telefono="63312435")

#gerente_creado = gerente_dao.create(gerente)
gerente_creado = control_gerente.create(gerente)
print(gerente_creado.gerente_id)  # El ID del gerente creado

#gerentes = gerente_dao.get_all()
gerentes = control_gerente.get_all()
print(gerentes[0].nombre)  # Lista de todos los gerentes

#gerente_obtenido = gerente_dao.get(1)
gerente_obtenido = control_gerente.get(1)
print(gerente_obtenido.correo_electronico)  # Nombre del gerente obtenido

gerente_obtenido.correo_electronico = "manuel.corral248399@potros.itson.edu.mx"
#gerente_actualizado = gerente_dao.update(gerente_obtenido)
gerente_actualizado = control_gerente.update(gerente_obtenido)
print(gerente_actualizado.correo_electronico)  # Edad actualizada del gerente


#gerente_dao.delete(gerente_actualizado)
control_gerente.delete(gerente_actualizado)




