#Encripta la clave del usuario (reversa + string extra si 'indice caracter' es par)
def hashClave(claveLimpia:str):
    claveEncriptada = ""
    for i in range(len(claveLimpia)-1, -1, -1):#Desde -1 y restando (reversa)
      claveEncriptada += claveLimpia[i] if i%2 else f"[{claveLimpia[i]}]3NCR1PT@D0"
    return claveEncriptada
  
 
#Solicita informacion al usuario con un mensaje y un tipo de dato especifico. Se pueden agregar opcioens validas 
def solicitarInformacion(mensaje:str, tipoDeDato: type = str, opcionesValidas:list = None):
  if tipoDeDato not in (int, str):
    raise TypeError("Solo se aceptan tipos 'str' o 'int'")
  
  while True:
    valor = input(mensaje).strip()
    
    if tipoDeDato is int:
      if not valor.isdigit():
        print('Ingrese un dato numerico')
        continue #'Volve a empezar'
      valor = int(valor) #Si requerimos int -> parseamos
     
    if opcionesValidas and valor not in opcionesValidas:
      print(f"Valor no permitido, ingrese una opcion valida: {opcionesValidas}")  
      continue #'Volve a empezar'
    
    return valor #Matamos al while infinito
    
      
      
        
   
  