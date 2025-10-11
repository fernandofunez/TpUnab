#Orquestador de los ELEMENTOS de la aplicacion
#NO ES EL ARRANQUE. Es el orquestador --> Meneja: Usuarios, Envio de mensajes, creacion/logueo de usuario, etc

from servidorCorreo import ServidorCorreo
from usuario import Usuario
from mensaje import Mensaje
from interfazDeUsuario import InterfazDeUsuario
from herramientas import (hashClave, solicitarInformacion)
from carpeta import Carpeta


class SistemaEmail():
  def __init__(self):
    self.servidores:list[ServidorCorreo] = []
    self.usuarioAutenticado = None
    self.interfaz:InterfazDeUsuario = InterfazDeUsuario()
    pass
  
  #Punto de entrada a la aplicacion
  def iniciarAplicacion(self):
    self._iniciarServidores()
    
    #Esto en bucle
    while True:
      self._autenticarUsuario()
      self._utilizarApp()
    
  def _iniciarServidores(self):
    servidor1 = ServidorCorreo('Servidor_1')
    servidor1.agregarUsuarioAlServidor(Usuario('Juan Perez', 'juanperez@gmail.com', '12345678'))
    servidor1.agregarUsuarioAlServidor(Usuario('Test', 'test@test.com', 'test'))
    servidor2 = ServidorCorreo('Servidor_1')
    servidor2.agregarUsuarioAlServidor(Usuario('Pedro Gomez', 'pedrogomez@gmail.com', '12345678'))
    servidor2.agregarUsuarioAlServidor(Usuario('Teo Pascual', 'teopascual@test.com', '12345678'))
    self.servidores.append(servidor1)
    self.servidores.append(servidor2)
      
  #Bucle para autenticacion del usuario    
  def _autenticarUsuario(self):
    while not isinstance(self.usuarioAutenticado, Usuario):
      #Mientras no haya usuario, se queda en el bucle de login
      self.interfaz.mostrarOpcionesLogin()
      eleccion = solicitarInformacion('> ', int, [1, 2, 0])
      if(eleccion == 1):
        self._iniciarSesion()
      elif(eleccion == 2):
        self._registrarse()
      elif(eleccion == 0):
        self.interfaz.mostrarFinAplicacion()
        exit()
    
  
  #Define el menu principal por el que se movera el usuario  
  def _utilizarApp(self):
    while True:
      self.interfaz.mostrarMenuApp(self.usuarioAutenticado.nombre)
      eleccion = solicitarInformacion('> ', int, [1, 2, 3, 4, 0])
      
      if(eleccion == 1):#Crear carpeta en mi usuario
        self.interfaz.mostrarEleccion(1)
        self._agregarNuevaCarpeta()
      elif(eleccion == 2):#Mostrar mis carpetas
        self.interfaz.mostrarEleccion(2)
        self._mostrarCarpetas()
      elif(eleccion == 3):#Enviar Mensaje
        self.interfaz.mostrarEleccion(3)
        self._iniciarEnvioMensaje()
      elif(eleccion == 4):#Mover un mensaje existente entre carpetas
        self._iniciarMoverMensaje()
        self.interfaz.mostrarEleccion(4)
      elif(eleccion == 0):
        self.interfaz.mostrarEleccion(0)
        self._cerrarSesion()
        return
  
  def _registrarse(self):
    nombre = solicitarInformacion('Ingrese nombre de usuario: > ', str)
    correo = solicitarInformacion('Ingrese correo de email: > ', str)
    clave = solicitarInformacion('Ingrese clave de usuario: > ', str)
    
    if correo == 'test': #if no existe el usuario en el sistema --> agregar
      self.interfaz.mostrarFalloRegistrarseUsuarioRepetido()
    else:
      nuevoUsuario = Usuario(nombre, correo, clave)
      self.servidores[0].agregarUsuarioAlServidor(nuevoUsuario)#TODO DEFINIR USO EN LA CLASE DE 'GRAFOS'. De que forma agregamos usuarios al sistema?
      self.interfaz.mostrarExitoRegistrarse()
      
  def _iniciarSesion(self):
    correo:str = solicitarInformacion('Ingrese correo de email: > ', str)
    clave = solicitarInformacion('Ingrese clave de usuario: > ', str)
    usuarioEncontrado = self._obtenerUsuarioPorCorreo(correo)
    if(isinstance(usuarioEncontrado, Usuario)):
      self.usuarioAutenticado = usuarioEncontrado if usuarioEncontrado.compararClaves(hashClave(clave)) else None
    else: 
      self.interfaz.mostrarErrorLogin()
  

  def _mostrarCarpetas(self):
    self.interfaz.mostrarArbolDeCarpetas(str(self.usuarioAutenticado.bandeja))
    
  def _agregarNuevaCarpeta(self):
    carpetasDisponibles:list[str] = []
    for carpeta in self.usuarioAutenticado.bandeja:
      carpetasDisponibles.append(carpeta.nombre)
    nuevaCarpeta:str = solicitarInformacion("Indique nombre de la nueva carpeta: > ", str)
    self.interfaz.mostrarListaCarpetas(carpetasDisponibles)
    carpetaPadre:str = solicitarInformacion('Indique carpeta destino: > ', str, carpetasDisponibles)
    resultado = self.usuarioAutenticado.agregarNuevaCarpeta(carpetaPadre, Carpeta(nuevaCarpeta))
    if(resultado): self.interfaz.mostrarCarpetaCreadaConExito(nuevaCarpeta)
    if(not resultado): self.interfaz.mostrarErrorAlCrearCarpeta()
    
  
  def _iniciarEnvioMensaje(self):
    destinatarios = self._obtenerCorreosDestinatariosDisponibles()
    
    self.interfaz.mostrarCorreosDestinatariosDisponibles(destinatarios)
    correoDestinatario = solicitarInformacion('Indique un correo destinatario: > ', str, destinatarios)
    asunto = solicitarInformacion('Asunto del mensaje: \n> ', str)
    cuerpo = solicitarInformacion('Cuerpo del mensaje: \n> ', str)
    
    usuarioRemitente = self.usuarioAutenticado
    usuarioDestinatario = self._obtenerUsuarioPorCorreo(correoDestinatario)
    
    nuevo_mensaje = Mensaje(asunto, cuerpo, usuarioRemitente.nombre, usuarioDestinatario.nombre, 0)

    usuarioRemitente.agregarMensajeEnviado(nuevo_mensaje)
    usuarioDestinatario.agregarMensaje(nuevo_mensaje)
    
    self.interfaz.mostrarAvisoMensajeEnviadoAUsuario(usuarioRemitente.nombre, usuarioDestinatario.nombre)
  
  
  def _obtenerCorreosDestinatariosDisponibles(self):
    correos:list[str] = []
    for servidor in self.servidores:
      correos.extend(servidor.listaDeCorreosDeUsuarios())
    return correos
    
  def _obtenerUsuarioPorCorreo(self, correo:str):
    usuarioEncontrado = None
    servidorIndex = 0
    while not isinstance(usuarioEncontrado, Usuario) and len(self.servidores) > servidorIndex:
      servidor = self.servidores[servidorIndex]
      usuarioEncontrado = servidor.buscarUsuarioPorCorreo(correo)
      servidorIndex+=1
    return usuarioEncontrado  
  
  def _iniciarMoverMensaje():
    return
    
  def _cerrarSesion(self):
    self.usuarioAutenticado = None  
    