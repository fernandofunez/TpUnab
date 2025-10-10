from usuario import Usuario

class ServidorCorreo():
  def __init__(self, nombreServidor):
    self.nombreServidor = nombreServidor
    self.usuarios:list[Usuario] = []
    pass
  
  
  def agregarUsuarioAlServidor(self, usuario):
    self.usuarios.append(usuario)
  
  
  def buscarUsuarioPorEmail(self, email:str):
    for usuario in self.usuarios:
      print(usuario.correo)
      print(usuario.correo == email)
      return usuario if usuario.correo == email else None  #Rompe el bucle. usar while mejor 
  
