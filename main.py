from entidades.sistemaEmail import SistemaEmail;
def main():
  miSistema = SistemaEmail()
  
  
  miSistema.iniciarSesion('fede@fede.com', '1234556')
  miSistema.enviarMensaje('test@test.com', "test", "test", "")
  print("FUNCIONA")
  
  
  
  
  
#Buena practica  
#Esto entiendo que es:
#Si mi archivo se llama MAIN entonces ejecutas main?? 
if __name__ == "__main__":
  main() 