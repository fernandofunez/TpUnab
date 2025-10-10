#Orquestador de los ELEMENTOS de la aplicacion
#NO ES EL ARRANQUE. Es el orquestador --> Meneja: Usuarios, Envio de mensajes, creacion/logueo de usuario, etc

from entidades.servidorCorreo import ServidorCorreo
from entidades.usuario import Usuario
from entidades.mensaje import Mensaje


class SistemaEmail():
  def __init__(self):
    #self.servidores = None La idea es que sea un grafo en un futuro
    self.servidores = [ServidorCorreo('Servidor_1'),ServidorCorreo('Servidor_2'),ServidorCorreo('Servidor_3')]
    self.usuarioAutenticado = None
    pass
  
  #Inicia sesion con un usuario
  def iniciarSesion(self, correo, clave):
    #Haces tu algoritmos y encontras: usuarioEncontrado
    #self.usuarioAutenticado = usuarioEncontrado
    self.usuarioAutenticado = Usuario('matias', 'matias@matias.com', '1234')
    pass
  
  #Crea un usuario
  #True --> se creo con exito
  #False --> hubo algun error
  def registrar(self, nombre, correo, contraseña, validarContraseña):
    if(contraseña != validarContraseña): return False
    #El email ya existe --> return False
    
    #Si esta todo ok, creas el usuario
    nuevoUsuario = Usuario(nombre, correo, contraseña)
    servidorMenosLleno = self.__retornarServidorMenosLleno()
    
    servidorMenosLleno.agregarUsuarioAlServidor(nuevoUsuario)
    
    #Ahora revisamos a que servidor agregarlo
    pass
  
  #Cierra sesion en el sistema
  def cerrarSesion(self):
    pass
  
  
  
  #Retorna False si fallo el envio
  #Retorna True si el envio se realizo
  def enviarMensaje(self, correoDestinatario, asunto, cuerpo, prioridad):
    if(self.usuarioAutenticado is None): return False
    usuarioDestinatario = self.__encontrarUsuarioEnLosServidores(correoDestinatario)
    if(usuarioDestinatario is None): return False
    
    
    #1-Creamos el mensaje
    nuevoMensaje = Mensaje(asunto, cuerpo, self.usuarioAutenticado.correo, usuarioDestinatario.correo, prioridad)
    #2-Enviar el mensaje
    usuarioDestinatario.agregarMensaje(nuevoMensaje)
    self.usuarioAutenticado.agregarMensajeEnviado(nuevoMensaje)
    
  
  #Crea una carpeta al usuario autenticado
  def crearNuevaCarpeta(self):
    if(self.usuarioAutenticado is None): return False
    pass
  
  #Revisa la bandeja del usuario autenticado
  def verBanedeja(self):
    if(self.usuarioAutenticado is None): return False
    self.usuarioAutenticado.verContenidoBandeja()
  
  #Busca en todos los servidores el usuario con ese correo
  def __encontrarUsuarioEnLosServidores(self, correo):
    return Usuario('fede', 'fede@fede.com', '1234')
  
  #Retorna el servidor menos lleno. Alfabeticamente
  def __retornarServidorMenosLleno(self):
    #DEFINIR ALGORITMO
    return self.servidores[0]#Para TEST
  
  
  
sis = SistemaEmail()  