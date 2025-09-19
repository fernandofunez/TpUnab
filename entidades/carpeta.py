class Carpeta():
  
  def __init__(self, nombre):
    self.nombre = nombre  
    self.subcarpetas = None
    self.mensajes = None
    #self.mensajes = [Mensaje("Prueba", "Esto es un mensaje"), Mensaje("Prueba 2", "Esto es otro mensaje")]
    
  #Agrega una suncarpeta a la carpeta  
  def crearSubcarpetas(self, nombre):
    pass
  
  #Agrega una mensaje a la carpeta
  def agregarMensaje(self, mensaje):
    pass
  
  #Lista todos los mensajes de la carpeta
  def listarMensajesDeCarpeta(self):
    #Si fuese un array y NO UN ARBOL, podriamos hacer algo asi
    #for mensaje in self.mensajes:
    #  print(mensaje)
    pass
  
  #Lista la carpeta actual y sus subcarpetas
  def listarCarpetas():
    pass
