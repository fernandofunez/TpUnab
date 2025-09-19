class Mensaje():
  def __init__(self, asunto, cuerpo, remitente, destinatario, prioridad):
    self.asunto = asunto
    self.cuerpo = cuerpo
    self.remitente = remitente
    self.destinatario = destinatario
    self.prioridad = prioridad
    
  def __str__(self):#Sobreescritura del metodo/accion 'mostrar en consola'
    return f"Asunto: {self.asunto} - Mensaje: {self.cuerpo}"
  

#Test    
#mensaje = Mensaje("prueba", "esto es una prueba", None, None, None)
#print(mensaje);   

