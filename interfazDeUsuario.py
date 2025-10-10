class InterfazDeUsuario:
  #Esta clase la usamos como forma grafica. Podriamos agregar metodos estaticos para imprimir opciones del menu
  def __init__(self):
    pass
  
  
  
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
  
  def menuLogin(self):
     #//Bienvenido a no se donde
    #//Para comenzar a utilizar el sistema debe autenticarse
   #//1- Registrarse
    #//2- Loguearse
    print('\n')
    print('Bienvenido al Sistema Email\n')
    print('¿Que desea realizar?')
    print('1-      Iniciar sesion')
    print('2-      Registrarse')
    print('\n')

    #print('-----Bienvenido al Sistema Email-----')
    #print('--------¿Que desea realizar?-------')
    #print('-----------Registrarse------------')
    #print('----------Iniciar Sesion---------')

  
  def menuPrincipal(self, nombre:str):
    print(f"Bienvenido, {nombre}")
    print('¿Que desea realizar hoy?')
    print('1- Crear carpeta')
    print('2- Mostrar tus carpetas')
    print('3- Enviar Mensaje')
    print('4- Mover un mensajes entre carpetas')
    print('0-  Salir')
