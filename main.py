

from arbolCarpetas import ArbolCarpetas
from usuario import Usuario
from mensaje import Mensaje
def main():
  
  
  
  usuario = Usuario("fede", "fedebacelar@gmail.com", "12345678")
  
  usuario.listarCarpetas()
  usuario.listarContenidoDeCarpeta('Bandeja de entrada')
  usuario.agregarMensaje(Mensaje("Prueba forzada 1", "Esto es una prueba para forzar el funcionamiento interno de este metodo", "fede", "fede", 0), 'Bandeja de entrada')
  
  usuario.agregarMensaje(Mensaje("Prueba forzada 2", "Esto es una prueba para forzar el funcionamiento interno de este metodo", "fede", "fede", 0), 'Bandeja de entrada')
  
  usuario.agregarMensaje(Mensaje("Prueba forzada 3", "Esto es una prueba para forzar el funcionamiento interno de este metodo", "fede", "fede", 0), 'Bandeja de entrada')
  usuario.listarContenidoDeCarpeta('Bandeja de entrada')
  
  usuario
  
  aaaaaaa
 
 
  
  #miSistema.iniciarSesion('fede@fede.com', '1234556')
  #miSistema.enviarMensaje('test@test.com', "test", "test", "")
  #print("FUNCIONA")
  
  
  
  
  
#Buena practica  
#Esto entiendo que es:
#Si mi archivo se llama MAIN entonces ejecutas main?? 
if __name__ == "__main__":
  main() 