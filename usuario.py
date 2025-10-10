from carpeta import Carpeta
from arbolCarpetas import ArbolCarpetas
from mensaje import Mensaje
from herramientas import hashClave

class Usuario():
  def __init__(self, nombre:str, correo:str, clave:str):
    self.nombre:str = nombre
    self.correo:str = correo
    self._claveEncriptada:str = hashClave(clave)
    self._inicializarCorreo()
  
  def _inicializarCorreo(self):
    self.bandeja:ArbolCarpetas = ArbolCarpetas(Carpeta('Correo'))
    self.bandeja.insertar(Carpeta('Bandeja de entrada'), 'Correo')
    self.bandeja.insertar(Carpeta('Enviados'), 'Correo')
    self.bandeja.insertar(Carpeta('Borradores'), 'Correo')
  
  #Agrea un Mensaje a la carpeta destino
  def agregarMensaje(self, mensaje:Mensaje, nombreCarpetaDestino:str):
    carpetaDestino = self.bandeja.buscar(nombreCarpetaDestino)
    if isinstance(carpetaDestino, Carpeta):
      carpetaDestino.agregarMensaje(mensaje)
      return True
    return False
  
  #Guarda el mensaje en la carpetas 'enviados'
  def agregarMensajeEnviado(self, mensaje:Mensaje):
    NOMBRE_CARPETA_ENVIADOS = "Enviados"
    carpetaDestino = self.bandeja.buscar(NOMBRE_CARPETA_ENVIADOS)
    if isinstance(carpetaDestino, Carpeta):
      carpetaDestino.agregarMensaje(mensaje)
      return True
    return False
  
  def listarContenidoDeCarpeta(self, nombreCarpeta):
    carpeta = self.bandeja.buscar(nombreCarpeta)
    if not isinstance(carpeta, Carpeta): raise FileNotFoundError("Carpeta no encontrada")
    carpeta.listarMensajesDeCarpeta()
  
  #Muestra el arbol de carpetas
  def listarCarpetas(self):
    print(self.bandeja)
  
  def listarMensajePrioridad(self):
    pass
  
  
  def agregarNuevaCarpeta(self, nombreCarpetaPadre, nuevaCarpetaHija:Carpeta):
    if not isinstance(nuevaCarpetaHija, Carpeta): raise TypeError("nuevaCarpetaHija espera un tipo de dato Carpeta")
    exito = self.bandeja.insertar(nuevaCarpetaHija, nombreCarpetaPadre)
    return exito
  
  
  def compararClaves(self, claveHash:str):
    return claveHash == self._claveEncriptada
    
  
  
  
    
  
  
  
