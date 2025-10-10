#Orquestador de los ELEMENTOS de la aplicacion
#NO ES EL ARRANQUE. Es el orquestador --> Meneja: Usuarios, Envio de mensajes, creacion/logueo de usuario, etc

from servidorCorreo import ServidorCorreo
from usuario import Usuario
from mensaje import Mensaje
from interfazDeUsuario import InterfazDeUsuario
from herramientas import hashClave
from carpeta import Carpeta


class SistemaEmail():
  def __init__(self):
    self.servidores:list[ServidorCorreo] = []
    self.usuarioAutenticado = None
    self.interfaz:InterfazDeUsuario = InterfazDeUsuario()
    pass
  
  def iniciarAplicacion(self):
    self._iniciarServidores()
    self._autenticar()
    self._opcionesApp()
    
  
  
  def _autenticar(self):
    while not isinstance(self.usuarioAutenticado, Usuario):
      #Mientras no haya usuario, se queda en el bucle de login
      self.interfaz.menuLogin()
      accionDeUsuario = str(input("Opcion: "))
      print(accionDeUsuario)
      
      
      if(accionDeUsuario == '1'):
        self.usuarioAutenticado = self._iniciarSesion()
      elif(accionDeUsuario == '2'):
        self.usuarioAutenticado = self._registrarse()
      else:
        print('No existe esa opcion')
        
      if(not isinstance(self.usuarioAutenticado, Usuario)): print('\n--------No fue posible autenticarse--------\n')  

    print('Usuario autenticado con exito')  
        
        
      
  def _registrarse(self):
    print('Elegiste la opcion de registrarse')
    nombre = input("Nombre: ")
    correo = input("Correo: ")
    clave = input("Clave: ")
    nuevoUsuario = Usuario(nombre, correo, clave)
    self.servidores[0].agregarUsuarioAlServidor(nuevoUsuario)#TODO DEFINIR USO EN LA CLASE DE 'GRAFOS' (ARRAY 0 PUEDE ROMPER)
    return nuevoUsuario
    
  
  def _iniciarSesion(self):
    print('Elegiste la opcion de iniciar sesion')
    email:str = str(input("Email: "))
    clave = str(input("Clave: "))
    usuarioEncontrado = None
    servidorIndex = 0
    while not isinstance(usuarioEncontrado, Usuario) and len(self.servidores) > servidorIndex:
      servidor = self.servidores[servidorIndex]
      usuarioEncontrado = servidor.buscarUsuarioPorEmail(email)
      servidorIndex+=1
    if(isinstance(usuarioEncontrado, Usuario)):
      return usuarioEncontrado if usuarioEncontrado.compararClaves(hashClave(clave)) else None
    
    return None
  
  
  def _opcionesApp(self):
    salir = False
    
    while not salir:
      self.interfaz.menuPrincipal(self.usuarioAutenticado.nombre)
      accionDeUsuario = str(input("Opcion: "))#Pido accion
      
      if(accionDeUsuario == '1'):#Crear carpeta en mi usuario
        self._agregarNuevaCarpeta()
        
        pass
      elif(accionDeUsuario == '2'):#Mostrar mis carpetas
        self._mostrarCarpetas()
        pass
      elif(accionDeUsuario == '3'):#Enviar Mensaje
        pass
      elif(accionDeUsuario == '4'):#Mover un mensaje existente entre carpetas
        pass
      elif(accionDeUsuario == '0'):
        salir = True
      else:
        print('No existe esa opcion')

  def _mostrarCarpetas(self):
    print(self.usuarioAutenticado.bandeja)

  def _agregarNuevaCarpeta(self):
    carpetaPadre = input("Nombre de la carpeta Padre: ")
    nuevaCarpeta = input("Nombre de la nueva carpeta: ")
    
    resultado = self.usuarioAutenticado.agregarNuevaCarpeta(carpetaPadre, Carpeta(nuevaCarpeta))
    if(resultado): print('Carpeta creada con exito')
    if(not resultado): print('Ocurrio un error al insertar la carpeta')
    self._mostrarCarpetas()
  
  def _iniciarServidores(self):
    servidor1 = ServidorCorreo('Servidor_1')
    servidor1.agregarUsuarioAlServidor(Usuario('Juan Perez', 'juanperez@gmail.com', '12345678'))
    servidor1.agregarUsuarioAlServidor(Usuario('Test', 'test@test.com', 'test'))
    servidor2 = ServidorCorreo('Servidor_1')
    servidor2.agregarUsuarioAlServidor(Usuario('Pedro Gomez', 'pedrogomez@gmail.com', '12345678'))
    servidor2.agregarUsuarioAlServidor(Usuario('Teo Pascual', 'teopascual@test.com', '12345678'))
    self.servidores.append(servidor1)
    self.servidores.append(servidor2)
    
    
  
  
  #//Bienvenido a no se donde
  #//Para comenzar a utilizar el sistema debe autenticarse
  #//1- Registrarse
  #//2- Loguearse
  
  
  #//Bienvenido Federico Bacelar
  #Que desea hacer??
  #
  #1- Gestionar Correo
  # 1.1-Crear Carpeta
  # 1.2-Mostrar arbol de carpetas
  # 1.3-Mover Mensajes de una carpeta a otra
  #
  #2- Mensajeria
  #2.1- Enviar mensaje
  # 
  #
  #
  #
  #
  #
  #
  #
  #
  #
  
  
  
  
  
  

  
  #Crea un usuario
  #True --> se creo con exito
  #False --> hubo algun error
  def _registrar(self, nombre, correo, contraseña, validarContraseña):
    if(contraseña != validarContraseña): return False
    #El email ya existe --> return False
    
    #Si esta todo ok, creas el usuario
    nuevoUsuario = Usuario(nombre, correo, contraseña)
    servidorMenosLleno = self.__retornarServidorMenosLleno()
    
    servidorMenosLleno.agregarUsuarioAlServidor(nuevoUsuario)
    
    #Ahora revisamos a que servidor agregarlo
    pass
  
  #Cierra sesion en el sistema
  def _cerrarSesion(self):
    pass
  
  
  
  #Retorna False si fallo el envio
  #Retorna True si el envio se realizo
  def _enviarMensaje(self, correoDestinatario, asunto, cuerpo, prioridad):
    if(self.usuarioAutenticado is None): return False
    usuarioDestinatario = self.__encontrarUsuarioEnLosServidores(correoDestinatario)
    if(usuarioDestinatario is None): return False
    
    
    #1-Creamos el mensaje
    nuevoMensaje = Mensaje(asunto, cuerpo, self.usuarioAutenticado.correo, usuarioDestinatario.correo, prioridad)
    #2-Enviar el mensaje
    usuarioDestinatario.agregarMensaje(nuevoMensaje)
    self.usuarioAutenticado.agregarMensajeEnviado(nuevoMensaje)
    
  
  #Crea una carpeta al usuario autenticado
  def _crearNuevaCarpeta(self):
    if(self.usuarioAutenticado is None): return False
    pass
  
  #Revisa la bandeja del usuario autenticado
  def _verBanedeja(self):
    if(self.usuarioAutenticado is None): return False
    self.usuarioAutenticado.verContenidoBandeja()
  
  #Busca en todos los servidores el usuario con ese correo
  def _encontrarUsuarioEnLosServidores(self, correo):
    return Usuario('fede', 'fede@fede.com', '1234')
  
  #Retorna el servidor menos lleno. Alfabeticamente
  def _retornarServidorMenosLleno(self):
    #DEFINIR ALGORITMO
    return self.servidores[0]#Para TEST
  
  
  
sis = SistemaEmail()  