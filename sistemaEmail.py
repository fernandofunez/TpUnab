from servidorCorreo import ServidorCorreo
from usuario import Usuario
from mensaje import Mensaje
from interfazDeUsuario import InterfazDeUsuario
from herramientas import (hashClave, solicitarInformacion)
from carpeta import Carpeta
from servidores import Servidores

class SistemaEmail():
  def __init__(self):
    self.servidores:Servidores
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
    self.servidores = Servidores()

    servidor1 = ServidorCorreo('S1')
    servidor2 = ServidorCorreo('S2')
    servidor3 = ServidorCorreo('S3')
    servidor4 = ServidorCorreo('S4')
    servidor5 = ServidorCorreo('S5')

    for servidor in (servidor1, servidor2, servidor3, servidor4, servidor5):
      self.servidores.agregarServidor(servidor)

    servidor1.agregarUsuarioAlServidor(Usuario('Ana',   'ana@s1.com',   '123'))
    servidor2.agregarUsuarioAlServidor(Usuario('Bruno', 'bruno@s2.com', '123'))
    servidor3.agregarUsuarioAlServidor(Usuario('Cami',  'cami@s3.com',  '123'))
    servidor4.agregarUsuarioAlServidor(Usuario('Dino',  'dino@s4.com',  '123'))
    servidor5.agregarUsuarioAlServidor(Usuario('Eva',   'eva@s5.com',   '123'))


    self.servidores.agregarConexion(servidor1, servidor2, 10)
    self.servidores.agregarConexion(servidor2, servidor3, 8)
    self.servidores.agregarConexion(servidor3, servidor4, 6)
    self.servidores.agregarConexion(servidor4, servidor5, 9)

    self.servidores.agregarConexion(servidor1, servidor3, 22)
    self.servidores.agregarConexion(servidor2, servidor4, 12)
    self.servidores.agregarConexion(servidor1, servidor4, 26)
    self.servidores.agregarConexion(servidor1, servidor5, 35)

      
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
      eleccion = solicitarInformacion('> ', int, [1, 2, 3, 4, 5, 0])
      
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
      elif eleccion == 5:
        self.interfaz.mostrarEleccion(5)
        self._iniciarCrearFiltro()  
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
      self.servidores.agregarUsuarioEnServidorAleatorio(nuevoUsuario)
      self.interfaz.mostrarExitoRegistrarse()
      
  def _iniciarSesion(self):
    correo:str = solicitarInformacion('Ingrese correo de email: > ', str)
    clave = solicitarInformacion('Ingrese clave de usuario: > ', str)
    usuarioEncontrado = self.servidores.buscarUsuarioPorCorreo(correo)
    if(isinstance(usuarioEncontrado, Usuario)):
      self.usuarioAutenticado = usuarioEncontrado if usuarioEncontrado.compararClaves(hashClave(clave)) else None
    else: 
      self.interfaz.mostrarErrorLogin()
  

  def _mostrarCarpetas(self):
    self.interfaz.mostrarArbolDeCarpetas(str(self.usuarioAutenticado.bandeja))
    
  def _agregarNuevaCarpeta(self):
    carpetasDisponibles:list[str] = self._obtenerNombreDeCarpetasDisponibles()
    nuevaCarpeta:str = solicitarInformacion("Indique nombre de la nueva carpeta: > ", str)
    self.interfaz.mostrarListaCarpetas(carpetasDisponibles)
    carpetaPadre:str = solicitarInformacion('Indique carpeta destino: > ', str, carpetasDisponibles)
    resultado = self.usuarioAutenticado.agregarNuevaCarpeta(carpetaPadre, Carpeta(nuevaCarpeta))
    if(resultado): self.interfaz.mostrarCarpetaCreadaConExito(nuevaCarpeta)
    if(not resultado): self.interfaz.mostrarErrorAlCrearCarpeta()
    
  
  def _iniciarEnvioMensaje(self):
    destinatarios = self.servidores.obtenerCorreosDestinatariosDisponibles()
    self.interfaz.mostrarCorreosDestinatariosDisponibles(destinatarios)
    correoDestinatario = solicitarInformacion('Indique un correo destinatario: > ', str, destinatarios)
    asunto = solicitarInformacion('Asunto del mensaje: \n> ', str)
    cuerpo = solicitarInformacion('Cuerpo del mensaje: \n> ', str)
    costoTotal = self.servidores.enviarMensaje(self.usuarioAutenticado.correo, correoDestinatario, asunto, cuerpo,  0)
  
    if costoTotal is not None:
      self.interfaz.mostrarAvisoMensajeEnviadoAUsuario(self.usuarioAutenticado.correo, correoDestinatario, costoTotal)
    else:
      print("No se pudo enviar el mensaje")  

    
  
  def _iniciarMoverMensaje(self):
    seleccion = self._obtenerMensajeNavegando()
    if seleccion is None: return
    
    carpetaOrigen:Carpeta = seleccion["carpeta"]
    mensaje:Mensaje = seleccion["mensaje"]
    
    self.interfaz.mostrarSeleccionMensajeParaMover(carpetaOrigen.nombre, mensaje.asunto)
    carpetasDisponibles:list[str] = self._obtenerNombreDeCarpetasDisponibles()
    self.interfaz.mostrarListaCarpetas(carpetasDisponibles)
    carpetaDestinoSeleccionada:str = solicitarInformacion('Indique carpeta destino: > ', str, carpetasDisponibles)
    
    carpetaDestino = self.usuarioAutenticado.bandeja.buscar(carpetaDestinoSeleccionada)
    if(isinstance(carpetaDestino, Carpeta)):
      carpetaOrigen.eliminarMensaje(mensaje)
      carpetaDestino.agregarMensaje(mensaje)
    return
  
  def _iniciarCrearFiltro(self):
    carpetas = self._obtenerNombreDeCarpetasDisponibles()
    self.interfaz.mostrarListaCarpetas(carpetas)
    carpetaDestino = solicitarInformacion("Carpeta destino del filtro: > ", str, carpetas)

    propiedades = ["remitente", "asunto"]  # Propiedades permitidas (DEBEN ESTAR EN EL OBJETO MENSAJE)
    print("\nCampos disponibles para filtrar:")
    for p in propiedades:
      print(" -", p)

    propiedad = None
    while propiedad not in propiedades:
      propiedad = solicitarInformacion("Indique la propiedad a filtrar: > ", str)
      if propiedad not in propiedades:
        print(f"'{propiedad}' no es valida. Intente nuevamente.\n")

    valor = solicitarInformacion("Valor del filtro: > ", str)

    self.usuarioAutenticado.agregarFiltro(propiedad, valor, carpetaDestino)
    print(f"\nFiltro creado correctamente: {propiedad} == '{valor}' → {carpetaDestino}")



  
  
  
  
  def _obtenerMensajeNavegando(self):
    mensaje = None
    salir = False
    
    archivos = self.usuarioAutenticado.bandeja
    carpetaActual = archivos.raiz.valor
    
    while not salir and not isinstance(mensaje, Mensaje): 
      carpetaPadre = archivos.obtenerCarpetaPadre(carpetaActual.nombre)
      carpetasHijas = archivos.obtenerCarpetasHijas(carpetaActual.nombre)
      mensajesEnCarpetaActual:list[Mensaje] = carpetaActual.mensajes

      self.interfaz.mostrarUbicacionActual(carpetaActual.nombre)
        
      if carpetaPadre:
        self.interfaz.mostrarOpcionRetroceso(carpetaPadre.nombre)
      if carpetasHijas:
          self.interfaz.mostrarSubcarpetasDisponibles([c.nombre for c in carpetasHijas])
      self.interfaz.mostrarMensajesEnCarpeta(mensajesEnCarpetaActual)

      self.interfaz.mostrarOpcionesDeNavegacion(carpetaPadre is not None, len(carpetasHijas) > 0, len(mensajesEnCarpetaActual) > 0)

      accion = solicitarInformacion("Seleccione una accion > ", str).strip().lower()

      if accion == "x":
        salir = True
        self.interfaz.mostrarSalidaDeNavegacion()        
      elif accion == ".." and carpetaPadre:
        carpetaActual = carpetaPadre
            
      elif accion.isdigit():
        indice = int(accion) - 1
        if 0 <= indice < len(carpetasHijas):    
          carpetaActual = carpetasHijas[indice]
        else:
          self.interfaz.mostrarOpcionInvalida()
                
      elif accion.startswith("m"):
        try:
          indice = int(accion[1:]) - 1 #'m12' -> 12
          if 0 <= indice < len(mensajesEnCarpetaActual):
            mensaje:Mensaje = mensajesEnCarpetaActual[indice]
            self.interfaz.mostrarMensajeSeleccionado(mensaje.asunto)
          else:
            self.interfaz.mostrarOpcionInvalida()
        except ValueError:
          self.interfaz.mostrarOpcionInvalida()
      else:
        self.interfaz.mostrarOpcionInvalida()
    return {"mensaje": mensaje, "carpeta": carpetaActual} if mensaje else None
  
  def _obtenerNombreDeCarpetasDisponibles(self):
    carpetasDisponibles:list[str] = []
    for carpeta in self.usuarioAutenticado.bandeja:
      carpetasDisponibles.append(carpeta.nombre)
    return carpetasDisponibles
    
  def _cerrarSesion(self):
    self.usuarioAutenticado = None  
    