from mensaje import Mensaje
from colaDeMensajes import ColaDeMensajes

class Carpeta():
  
  def __init__(self, nombre):
    self.nombre: str = nombre
    self.mensajes: ColaDeMensajes = ColaDeMensajes()
  
  def agregarMensaje(self, mensaje: Mensaje):
    self.mensajes.encolar(mensaje)
  
  def listarMensajesDeCarpeta(self):
    self.mensajes.listar()
  
  def eliminarMensaje(self, mensaje: Mensaje):
    return self.mensajes.eliminar(mensaje)
  
  def __str__(self):
    return self.nombre
  
  def __eq__(self, value):
    if isinstance(value, Carpeta):
      return value.nombre == self.nombre
    return False
