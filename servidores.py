from servidorCorreo import ServidorCorreo
from usuario import Usuario
from mensaje import Mensaje
import random


class Servidores:
  
  def __init__(self): #Inicia los servidores
    self.servidores: list[ServidorCorreo] = []
    self.conexiones: list[list[float | None]] = self._generarMatrizCuadrada(0)
    
  
  def _generarMatrizCuadrada(self, tamaño) -> list[list[None | float]]:
    return [[None]*tamaño for i in range(tamaño)]
  
  #Devuelve el indice del servidor en la lista o -1 si no se encuentra
  def _indice(self, servidor:ServidorCorreo):
    for i, s in enumerate(self.servidores):
      if(s == servidor):
        return i
    return -1  
  
  #Aumentan las conexiones para un nuevo servidor sin perder los datos anteriores
  def _expandirConexiones(self):
    cantidadServidoresViejo = len(self.conexiones)
    cantidadServidoresNuevo = cantidadServidoresViejo + 1
    
    nuevasConexiones = self._generarMatrizCuadrada(cantidadServidoresNuevo)
    for fila in range(cantidadServidoresViejo):
      for columna in range(cantidadServidoresViejo):
        nuevasConexiones[fila][columna] = self.conexiones[fila][columna]
    self.conexiones = nuevasConexiones
  
  #Indica si un servidor ya esta registrado
  def existe(self, servidor:ServidorCorreo):
    return self._indice(servidor) != -1
  
  def agregarServidor(self, servidor: ServidorCorreo):
    if self.existe(servidor):
      return False
    self.servidores.append(servidor)
    self._expandirConexiones()
    return True
  
  #Crea una conexion entre dos servidores usando un costo de conectividad indicado
  def agregarConexion(self, servidorA: ServidorCorreo, servidorB: ServidorCorreo, costoDeConectividad):
    if costoDeConectividad is None or costoDeConectividad <= 0:
      raise ValueError("El costo de conectividad debe ser positivo (ms)")
    indiceServidorA = self._indice(servidorA)
    indiceServidorB = self._indice(servidorB)
    if indiceServidorA == -1 or indiceServidorB == -1:
      raise ValueError("Ambos servidores deben existir para generar una conexion")
    if indiceServidorA == indiceServidorB:
      raise ValueError("No se puede conectar un servidor consigo mismo")
    self.conexiones[indiceServidorA][indiceServidorB] = costoDeConectividad
    self.conexiones[indiceServidorB][indiceServidorA] = costoDeConectividad
  
  def verConexiones(self): #Genera una representacion en texto de las conexiones entre servidores
    servidores = [servidor.nombreServidor for servidor in self.servidores]
    lineas = []
    header = "      " + " | ".join(f"{n[:6]:>6}" for n in servidores)
    lineas.append(header)
    lineas.append("-" * len(header))
    
    for i, fila in enumerate(self.conexiones):
      linea = f"{servidores[i][:6]:>6} " + " | ".join(f"{(c if c is not None else '.'):>6}" for c in fila)
      lineas.append(linea)
    return "\n".join(lineas)
  
  def _buscarServidorDeUsuario(self, correo:str) -> tuple[int, Usuario] | tuple[int, None]:
    for indice, servidor in enumerate(self.servidores):
      usuario = servidor.buscarUsuarioPorCorreo(correo)
      if usuario is not None:
        return indice, usuario
    return -1, None
  
  #Obtiene el costo minimo y la ruta entre dos servidores (dijkstra)
  def _dijkstra(self, indiceServidorOrigen: int, indiceServidorDestino: int) -> tuple[float, list[int]]:
    cantidadServidores = len(self.servidores)
    servidoresVisitados = [False] * cantidadServidores
    costoAcumulado = [float("inf")] * cantidadServidores
    servidorAnterior = [-1] * cantidadServidores
    costoAcumulado[indiceServidorOrigen] = 0.0

    for _ in range(cantidadServidores):
      servidorActual = -1
      menorCosto = float("inf")

      for i in range(cantidadServidores):
        if not servidoresVisitados[i] and costoAcumulado[i] < menorCosto:
          menorCosto = costoAcumulado[i]
          servidorActual = i

      if servidorActual == -1 or servidorActual == indiceServidorDestino:
        break

      servidoresVisitados[servidorActual] = True

      for indiceVecino in range(cantidadServidores):
        costoConexion = self.conexiones[servidorActual][indiceVecino]
        if costoConexion is None or servidoresVisitados[indiceVecino]:
          continue

        nuevoCosto = costoAcumulado[servidorActual] + costoConexion
        if nuevoCosto < costoAcumulado[indiceVecino]:
          costoAcumulado[indiceVecino] = nuevoCosto
          servidorAnterior[indiceVecino] = servidorActual

    if costoAcumulado[indiceServidorDestino] == float("inf"):
      return float("inf"), []

    rutaServidores: list[int] = []
    servidorActual = indiceServidorDestino
    while servidorActual != -1:
      rutaServidores.append(servidorActual)
      servidorActual = servidorAnterior[servidorActual]
    rutaServidores.reverse()

    return costoAcumulado[indiceServidorDestino], rutaServidores


#Localiza los servidores y usuarios involucrados en el envio
  def enviarMensaje(self, correoOrigen: str, correoDestino:str, asunto, cuerpo, prioridad):
    servidorOrigen, usuarioOrigen = self._buscarServidorDeUsuario(correoOrigen)
    servidorDestino, usuarioDestino = self._buscarServidorDeUsuario(correoDestino)
    
    #Valida la existencia del remitente y destinatario
    if(servidorOrigen == -1 or usuarioOrigen is None):
      print(f"No se encontro el remitente {correoOrigen} en ningun servidor.")
      return None
    if(servidorDestino == -1 or usuarioDestino is None):
      print(f"No se encontro el destinatario {correoDestino} en ningun servidor.")
      return None
    
    nuevoMensaje = Mensaje(asunto, cuerpo, usuarioOrigen.correo, usuarioDestino.correo, prioridad)
    
    if servidorOrigen == servidorDestino:
      costo_total = 0.0
    else: #Busca la ruta de menos entre servidores
      costo, camino = self._dijkstra(servidorOrigen, servidorDestino)
      if costo == float("inf") or not camino:
        print("No hay conectividad entre los servidores de origen y destino.")
        return None
      costo_total = costo

    #Registra el mensaje en enviados y lo entrega al destinatario
    usuarioOrigen.agregarMensaje(nuevoMensaje, 'Enviados', True)
    usuarioDestino.agregarMensaje(nuevoMensaje)

    return costo_total
  
  def agregarUsuarioEnServidorAleatorio(self, usuario: Usuario):
    servidor = random.choice(self.servidores)
    servidor.agregarUsuarioAlServidor(usuario)
    
  def obtenerCorreosDestinatariosDisponibles(self):
    correos: list[str] = []
    for servidor in self.servidores:
      for usuario in servidor.usuarios:
        correos.append(usuario.correo)
    return correos

  def buscarUsuarioPorCorreo(self, correo: str):
    usuarioEncontrado = None
    servidorIndex = 0
    while not isinstance(usuarioEncontrado, Usuario) and len(self.servidores) > servidorIndex:
      servidor = self.servidores[servidorIndex]
      usuarioEncontrado = servidor.buscarUsuarioPorCorreo(correo)
      servidorIndex+=1
    return usuarioEncontrado  
    


    
    