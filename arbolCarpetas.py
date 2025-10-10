from carpeta import Carpeta;

class NodoCarpeta():
    def __init__(self, valor: Carpeta):
        self.valor:Carpeta = valor #En este caso 'carpeta'
        self.hijos:list[NodoCarpeta] = [] #Array de otras carpetas
        
    #Recorrido en PreOrder (Primero padre, despues hijo INTENTA acceder al hijo izquierdo, repite)     
    def __iter__(self):
      yield NodoCarpeta(self.valor)
      for hijo in self.hijos:
        yield hijo


class ArbolCarpetas():

    def __init__(self, root:Carpeta):
      if not isinstance(root, Carpeta): raise ValueError("El valor inicial de ArbolCarpetas debe ser del tipo Carpeta")
      self.raiz:NodoCarpeta = NodoCarpeta(root)
    
    #Busca e inserta el un nuevo Nodo
    #Si la operacion fue exitosa, retorna True, caso contrario False
    def insertar(self, valor:Carpeta, nombreCarpeta:str): 
      nodoDestino = self._buscarRecursivo(nombreCarpeta, self.raiz)
      if not isinstance(nodoDestino, NodoCarpeta): return False
      nodoDestino.hijos.append(NodoCarpeta(valor))
      return True

    #Utiliza el metodo de comparacion (__eq__) para encontrar 
    # el valor de un nodo en forma recursiva iniciando por la raiz
    def buscar(self, nombreCarpeta:str):
      nodoEncontrado = self._buscarRecursivo(nombreCarpeta, self.raiz)
      if(isinstance(nodoEncontrado, NodoCarpeta)): return nodoEncontrado.valor
      return None

    #Busca el nodo en forma recursiva
    def _buscarRecursivo(self, nombreCarpeta:str, nodo:NodoCarpeta):
      if str(nodo.valor) == nombreCarpeta:
          return nodo
      return self._buscarEnHijos(nombreCarpeta, nodo.hijos)
    
    #Busca el nodo en los hijos
    def _buscarEnHijos(self, nombreCarpeta:str, hijos:list[NodoCarpeta]):
      for nodo in hijos:
        nodoEncontrado = self._buscarRecursivo(nombreCarpeta, nodo)
        if(isinstance(nodoEncontrado, NodoCarpeta)): return nodoEncontrado
      return None

    #Impresion en forma recursiva de sus hijos
    def _imprimirRecursivo(self, padre:NodoCarpeta, hijos:list[NodoCarpeta], profundidad:int, esUltimo:bool=False):
      lineas = [self._obtenerCadenaDelNodo(padre.valor, profundidad, esUltimo)]
      for hijo in hijos:
        esUltimoHijo = hijo is hijos[-1]
        lineas.extend(self._imprimirRecursivo(hijo, hijo.hijos, profundidad+1, esUltimoHijo))
      return lineas
    

    #Obtiene la cadena formateada
    def _obtenerCadenaDelNodo(self, nombreCarpeta:str, profundidad:int, esUltimo:bool):
      if profundidad == 0:
          return str(nombreCarpeta)
      return f"{'│  ' * (profundidad-1)}{'└─ ' if esUltimo else '├─ '}{nombreCarpeta}"
    
    
    #--------------------------------------------------------
    #----------------Sobrecarga de operadores----------------
    #--------------------------------------------------------
    
    def __str__(self):
      #Correo                 (profundidad 0) raiz
      #├─ Inbox               (profundidad 1)
      #│  ├─ Work             (profundidad 2)
      #│  │  ├─ Clients       (profundidad 3)
      #│  │  └─ Projects      (profundidad 3)
      #│  └─ Personal         (profundidad 2)
      #├─ Sent                (profundidad 1)
      #├─ Drafts              (profundidad 1)
      #└─ Trash               (profundidad 1)

      #los hijos se imprimen con: [-1]"└─ ", [otros]"├─ ", la separacion de profundidad con "│  "
      #Se imprime por cada operacion de acceso, se accede siempre a la izquierda del todo
      #La idea es crear un array al estilo:
      #["Correo","├─ Inbox","├─ Work", ....] y unirlos con un salto de linea (\n)
      #Al finalizar, hacemos el return
      listaDeCadenas = self._imprimirRecursivo(self.raiz, self.raiz.hijos, 0)
      return "\n".join(listaDeCadenas)
    
    def __iter__(self):
      if not isinstance(self.raiz, NodoCarpeta): raise SyntaxError("Error en la iteracion")
      for nodo in self.raiz:
        yield nodo.valor 