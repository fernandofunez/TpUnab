from textwrap import wrap

class Mensaje():
  def __init__(self, asunto, cuerpo, remitente, destinatario, prioridad):
    self.asunto = asunto
    self.cuerpo = cuerpo
    self.remitente = remitente
    self.destinatario = destinatario
    self.prioridad = prioridad
    
  #Sobreescritura del metodo str
  #Strings a utilizar: 
  # Bordes: "┏", "┓", "┗", "┛"
  # Separacion de bloques: "┣" "━" "┫"
  # Se utiliza un 'padding' de 1 caracter "  "
  # Con todos estos datos: 
  # Ejercicio --> Generar un algoritmo que retorne el 'string' del objeto Mensaje con un 'estilo de mensaje'
  # Nota: Utilizar '\n' para los saltos de linea, ej: "Linea uno\nLinea dos"
  #┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
  #┃                            MENSAJE                               ┃
  #┣━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┫
  #┃ Asunto: Prueba forzada 1                                         ┃
  #┃ De: fede                                                         ┃
  #┃ Para: fede                                                       ┃
  #┃ Prioridad: 0                                                     ┃
  #┣━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┫
  #┃ ──────────────────────────── CUERPO ──────────────────────────── ┃
  #┃ Esto es una prueba para forzar el funcionamiento interno de este ┃
  #┃ metodo                                                           ┃
  #┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛
  
  
  
  def __str__(self):
    prioridades = ["URGENTE", "IMPORTANTE", "NORMAL", "BAJA", "MUY BAJA"]

    if 1 <= self.prioridad <= 5:
        prioridad_texto = prioridades[self.prioridad - 1]
    else:
        prioridad_texto = "DESCONOCIDA"  
    return f"De: {self.remitente} | Para: {self.destinatario} | Asunto: {self.asunto} | Cuerpo: {self.cuerpo} | Prioridad: {prioridad_texto}"
     
  def __eq__(self, value):
    if not isinstance(value, Mensaje):
      return False
    return(
      self.asunto == value.asunto and
      self.cuerpo == value.cuerpo and
      self.remitente == value.remitente and
      self.destinatario == value.destinatario and
      self.prioridad == value.prioridad
    )
  

