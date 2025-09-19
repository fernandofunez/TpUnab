from entidades.carpeta import Carpeta

class Usuario():
  def __init__(self, nombre, correo, clave):
    self.nombre = nombre
    self.correo = correo
    self.__clave = clave
    self.bandeja = Carpeta("Bandeja_De_Entrada")
    pass
  
  #Esta funcion retorna un boolean
  #False --> si las credenciales son incorrectas
  #True --> si las credenciales son correctas
  def authenticarse(self, correo, clave):
    #Podriamos agregar una funcion de 'hasheo' --> "IDEA" no le den bola
    return (self.__clave == clave) and (self.correo == correo)
  
  def __hashClave():#--> "IDEA" no le den bola, es un metodo PRIVADO
    pass
  
  #Esta accion agrega un mensaje a el usuario Fer
  #Podriamos implementar reglas para saber a QUE CARPETA corresponde ese mensaje
  def agregarMensaje(self, mensaje):
    pass
  
  #Guarda el mensaje en la carpetas 'enviados'
  def agregarMensajeEnviado(self, mensaje):
    pass
  
  #Lista TODAS las carpetas + los mensajes
  
  def verContenidoBandeja():
    #EJEMPLO
    #-Bandeja_De_Entrada
    #   -Todos
    #     +Mensaje1
    #     +Mensaje2
    #     -CarpetaTrabajo
    #       +MensajeTrabajo1
    #       +MensajeTrabajo2
    #   -Spam
    #   -Enviados
    #     +MensajeEnviado1
    #
    #
    pass
  
  #Muestra solo los nombres de las carpetas (ejmplo)
  def verCarpetas():
    pass
  
  def listarMensajePrioridad():
    pass
  
  
    
  
  
  
    
  
  
  
  
  
  
#nuevoUsuario = Usuario('fede', 'fede@fede.ocm', '12345')  
#nuevoUsuario.clave --> ES PRIVADO, NO SE ACCEDE

def encontrarFer():
  pass

