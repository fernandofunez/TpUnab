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
    print("¿Qué desea realizar hoy?\n")
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
    print("Carpeta creada con éxito".center(self.ancho))
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


