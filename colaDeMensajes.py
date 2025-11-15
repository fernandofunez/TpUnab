from mensaje import Mensaje

class NodoMensaje:
  def __init__(self, dato:Mensaje):
    self.dato: Mensaje = dato
    self.siguiente: NodoMensaje | None = None

class ColaDeMensajes:
  
  def __init__(self):
    self.cursor: NodoMensaje | None = None   
    
  def estaVacia(self):
    return self.cursor is None

  #Inserta un mensaje dentro de la cola segun la importancia
  def encolar(self, mensaje: Mensaje):
    nuevo = NodoMensaje(mensaje)

    if self.cursor is None:
      self.cursor = nuevo
      return

    #Inserta al comienzo de la lista el mensaje con mayor prioridad
    if mensaje.prioridad < self.cursor.dato.prioridad:
      nuevo.siguiente = self.cursor
      self.cursor = nuevo
      return

    #Recorre la lista, manteniendo el orden por prioridad
    actual = self.cursor
    while (actual.siguiente is not None and
           actual.siguiente.dato.prioridad <= mensaje.prioridad):
      actual = actual.siguiente

    nuevo.siguiente = actual.siguiente
    actual.siguiente = nuevo
    
  #Obtiene y elimina el mensaje mas importante
  #Devuelve None si la cola esta vacia
  def desencolar(self):
    if self.cursor is None:
      return None

    dato = self.cursor.dato
    self.cursor = self.cursor.siguiente
    return dato

  #Elimina un mensaje especifico de la cola
  #True si fue eliminado, False si no se encontro
  def eliminar(self, mensaje: Mensaje) -> bool:
    if self.cursor is None:
      return False

    if self.cursor.dato == mensaje:
      self.cursor = self.cursor.siguiente
      return True

    anterior = self.cursor
    actual = self.cursor.siguiente

    while actual is not None:
      if actual.dato == mensaje:
        anterior.siguiente = actual.siguiente
        return True

      anterior = actual
      actual = actual.siguiente

    return False

  #Muestra todos los mensajes segun el orden de prioridad de la cola
  def listar(self):
    actual = self.cursor
    index = 1

    while actual is not None:
      print(f"{index}- {actual.dato}")
      actual = actual.siguiente
      index += 1  
  
  def __iter__(self):
    actual = self.cursor
    while actual is not None:
      yield actual.dato
      actual = actual.siguiente    
      
  def __len__(self):
    contador = 0
    actual = self.cursor
    while actual is not None:
      contador += 1
      actual = actual.siguiente
    return contador    
  
  #Permite obtener un mensaje usando un indice
  def __getitem__(self, index: int) -> Mensaje:
    if index < 0:
      raise IndexError("Indice negativo no soportado")

    actual = self.cursor
    i = 0

    while actual is not None and i < index:
      actual = actual.siguiente
      i += 1

    if actual is None:
      raise IndexError("Indice fuera de rango")

    return actual.dato
    