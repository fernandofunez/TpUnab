from sistemaEmail import SistemaEmail
def main():
  app = SistemaEmail()
  app.iniciarAplicacion()

if __name__ == "__main__":
  main() 
  
  
"""  
from grafo import Servidores
from servidorCorreo import ServidorCorreo
from usuario import Usuario

if __name__ == "__main__":
    # servidores
    sA = ServidorCorreo("A")
    sB = ServidorCorreo("B")
    sC = ServidorCorreo("C")
    sD = ServidorCorreo("D")

    # grafo
    red = Servidores()
    for s in (sA, sB, sC, sD):
        red.agregarServidor(s)

    # conexiones (ms)
    red.agregarConexion(sA, sB, 10)
    red.agregarConexion(sB, sC, 5)
    red.agregarConexion(sA, sC, 30)
    red.agregarConexion(sC, sD, 2)

    # usuarios
    sA.agregarUsuarioAlServidor(Usuario("test", "u1@a.com", "123"))
    sD.agregarUsuarioAlServidor(Usuario("test2", "u2@d.com", "123"))

    print(red.verConexiones())
    print(red.enviarMensaje("u1@a.com", "u2@d.com"))  
    
"""    