class InterfazDeUsuario:
  

  def __init__(self, ancho: int = 54):
    self.ancho = max(40, ancho)
        
  def _linea(self, char: str = "-"):
    print(char * self.ancho)

  def _titulo(self, texto: str):
    self._linea("=")
    print(texto.center(self.ancho))
    self._linea("=")

  def _bloque(self, subtitulo: str | None = None):
    if subtitulo:
      print(subtitulo)
      self._linea()

    # ---------- Pantallas ----------
  def mostrarOpcionesLogin(self):
    print("\n")
    self._titulo("SISTEMA DE EMAIL")
    print("Para comenzar, elija una opcion:\n")
    print("  1) Iniciar sesion")
    print("  2) Registrarse")
    print("  0) Salir")
    self._bloque("Ingrese el numero de opcion y presione 'Enter':")

  def mostrarErrorLogin(self):  
    print("\n")
    self._linea("!")
    print("No fue posible autenticarse. Revise los datos e intente nuevamente.")
    self._linea("!")

  def mostrarFinAplicacion(self):
    print("\n")
    self._linea("=")
    print("Fin de la aplicacion. ¡Gracias por usar el sistema!".center(self.ancho))
    self._linea("=")

  def mostrarMenuApp(self, nombre: str):
    print("\n")
    self._titulo(f"BIENVENIDO, {nombre}")
    print("¿Que desea realizar hoy?\n")
    print("  1) Crear carpeta")
    print("  2) Mostrar mis carpetas")
    print("  3) Enviar mensaje")
    print("  4) Mover mensajes entre carpetas")
    print("  0) Cerrar Sesion")
    self._bloque("Ingrese el numero de opciun y presione 'Enter':")
      
  def mostrarEleccion(self, opcion: int):
    print("\n")
    self._linea()
    print(f"Elegiste la opcion: {opcion}".center(self.ancho))
    self._linea()

  def mostrarExitoRegistrarse(self):
    print("\n")
    self._linea("=")
    print("Registro completado con exito".center(self.ancho))
    print("Ahora puede iniciar sesion para usar la aplicacion.".center(self.ancho))
    self._linea("=")    

  def mostrarFalloRegistrarseUsuarioRepetido(self):
    print("\n")
    self._linea("!")
    print("No fue posible completar el registro.".center(self.ancho))
    print("El email de usuario ya se encuentra en uso.".center(self.ancho))
    print("Por favor, intente con otro email.".center(self.ancho))
    self._linea("!")
   
  def mostrarArbolDeCarpetas(self, arbol: str):
    print("\n")
    self._linea("=")
    print("ARBOL DE CARPETAS".center(self.ancho))
    self._linea("-")
    print(arbol)
    self._linea("=")
   
  def mostrarListaCarpetas(self, carpetasDisponibles: list[str]):
    print("\n")
    self._linea("=")
    print("CARPETAS DISPONIBLES".center(self.ancho))
    self._linea("-")
    print(" - ".join(carpetasDisponibles))
    self._linea("=")

  def mostrarCarpetaCreadaConExito(self, nombreCarpeta: str):
    print("\n")
    self._linea("=")
    print("Carpeta creada con exito".center(self.ancho))
    print(f"'{nombreCarpeta}' ahora forma parte de tus carpetas.".center(self.ancho))
    self._linea("=")

  def mostrarErrorAlCrearCarpeta(self, nombreCarpeta: str):
    print("\n")
    self._linea("!")
    print("No se pudo crear la carpeta.".center(self.ancho))
    print(f"'{nombreCarpeta}' ya existe o el nombre no es válido.".center(self.ancho))
    print("Por favor, intente con otro nombre.".center(self.ancho))
    self._linea("!")
    
  def mostrarCorreosDestinatariosDisponibles(self, destinatarios: list[str]):
    print("\n")
    self._linea("=")
    print("CORREOS DE DESTINATARIOS DISPONIBLES".center(self.ancho))
    self._linea("-")
    for nombre in destinatarios:
      print(f"- {nombre}")
    self._linea("=")
    
  def mostrarAvisoMensajeEnviadoAUsuario(self, remitente: str, destinatario: str):
    print("\n")
    self._linea("=")
    print("MENSAJE ENVIADO".center(self.ancho))
    self._linea("-")
    print(f"El usuario '{remitente}' ha enviado un mensaje a '{destinatario}'.".center(self.ancho))
    self._linea("=")

  def mostrarUbicacionActual(self, nombreCarpeta: str):
    print("\n")
    self._titulo(f"CARPETA ACTUAL: {nombreCarpeta}")

  def mostrarOpcionRetroceso(self, nombrePadre: str):
    print(f"Puede volver a la carpeta superior: {nombrePadre}")

  def mostrarSubcarpetasDisponibles(self, nombres: list[str]):
    if not nombres:
      return
    print("\nSubcarpetas disponibles:")
    for i, nombre in enumerate(nombres, start=1):
      print(f"  {i}) {nombre}")

  def mostrarMensajesEnCarpeta(self, mensajes: list):
    print("\nMensajes en esta carpeta:")
    if not mensajes:
      print("  No hay mensajes disponibles.")
    else:
      for i, mensaje in enumerate(mensajes, start=1):
        print(f"  m{i}) {mensaje.asunto}")

  def mostrarOpcionesDeNavegacion(self, puedeRetroceder:bool, puedeAvanzar:bool, puedeSeleccionarMensaje:bool):
    self._linea("-")
    print("Opciones:")
    if puedeRetroceder :
      print("  ..  Retroceder a la carpeta superior")
    if puedeAvanzar :
      print("  <n>  Ingresar a una subcarpeta (ejemplo: 1)")
    if puedeSeleccionarMensaje : 
      print("  m<n> Seleccionar un mensaje (ejemplo: m1)")
    print("  x    Salir de la navegacion")
    self._linea("-")

  def mostrarOpcionInvalida(self):
    print("\nOpcion no valida. Intente nuevamente.")

  def mostrarMensajeSeleccionado(self, asunto: str):
    print("\n")
    self._linea("=")
    print("MENSAJE SELECCIONADO".center(self.ancho))
    self._linea("-")
    print(f"Se ha seleccionado el mensaje: '{asunto}'".center(self.ancho))
    self._linea("=")

  def mostrarSalidaDeNavegacion(self):
    print("\n")
    self._linea("=")
    print("Saliendo del navegador de carpetas...".center(self.ancho))
    self._linea("=")

  def mostrarSeleccionMensajeParaMover(self, carpetaOrigen: str, asuntoMensaje: str):
    print("\n")
    self._linea("=")
    print(f"Se selecciono de la carpeta '{carpetaOrigen}' el mensaje:".center(self.ancho))
    print(f"'{asuntoMensaje}'".center(self.ancho))
    self._linea("-")
    print("Ahora indique una carpeta de destino.".center(self.ancho))
    self._linea("=")
