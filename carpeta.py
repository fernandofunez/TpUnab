from mensaje import Mensaje

class Carpeta():
  
  def __init__(self, nombre):
    self.nombre:str = nombre
    self.mensajes:list[Mensaje] = []
  
  #Agrega una mensaje a la carpeta
  def agregarMensaje(self, mensaje: Mensaje):
    self.mensajes.append(mensaje)
  
  #Lista todos los mensajes de la carpeta
  def listarMensajesDeCarpeta(self):
    for mensaje in self.mensajes:
      print('\n')
      print(mensaje)
      print('\n') 
  
  def __str__(self):
    return self.nombre
  
  def __eq__(self, value):
    if isinstance(value, Carpeta):
      return value.nombre == self.nombre
    return False
