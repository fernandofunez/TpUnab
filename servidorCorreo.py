from usuario import Usuario

class ServidorCorreo():
  def __init__(self, nombreServidor):
    self.nombreServidor = nombreServidor
    self.usuarios:list[Usuario] = []
  
  
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
  
