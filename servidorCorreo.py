from usuario import Usuario

class ServidorCorreo():
  def __init__(self, nombreServidor):
    self.nombreServidor = nombreServidor
    self.usuarios:list[Usuario] = []
  #Inicia el servidor con un nombre y una lista vacia de usuarios
  
  def agregarUsuarioAlServidor(self, usuario:Usuario):
    self.usuarios.append(usuario)
    
  def listaDeCorreosDeUsuarios(self):
    correos:list[str] = []
    for usuario in self.usuarios:
      correos.append(usuario.correo)
    return correos
  
  
  def buscarUsuarioPorCorreo(self, email:str):
    for usuario in self.usuarios:
      if usuario.correo == email:
        return usuario
    return None
  
  def __eq__(self, servidor):
    return isinstance(servidor, ServidorCorreo) and self.nombreServidor == servidor.nombreServidor
  
  def __str__(self):
    return self.nombreServidor