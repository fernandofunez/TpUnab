class Nodo():
    def __init__(self, valor):
        self.valor = valor #En este caso 'carpeta'
        self.hijos = [] #Array de otras carpetas


class Arbol():

    def __init__(self):
        self.raiz = None
    
    #Busca e inserta el un nuevo Nodo
    #Si la operacion fue exitosa, retorna True, caso contrario False
    def insertar(self, valor, valorDestino):
        nodoDestino = self._buscarRecursivo(valorDestino, self.raiz)
        if nodoDestino is None: return False
        nodoDestino.hijos.append(Nodo(valor))

    #Utiliza el metodo de comparacion (__eq__) para encontrar 
    # el valor de un nodo en forma recursiva iniciando por la raiz
    def buscar(self, valor):
        if self.raiz is None: return None
        nodo = self._buscarRecursivo(valor, self.raiz)
        if(nodo is not None): return nodo.valor
        return None

    #Busca el nodo en forma recursiva
    def _buscarRecursivo(self, valor, nodo):
        if nodo.valor == valor:
            return nodo
        return self._buscarEnHijos(valor, nodo.hijos)
    
    #Busca el nodo en los hijos
    def _buscarEnHijos(self, valor, hijos):
        for nodo in hijos:
            nodoEncontrado = self._buscarRecursivo(valor, nodo)
            if nodoEncontrado is not None: return nodoEncontrado
        return None
    
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
        if(self.raiz is None): return ""
        listaDeCadenas = self.imprimirRecursivo(self.raiz, self.raiz.hijos, 0)
        return "\n".join(listaDeCadenas)

    def imprimirRecursivo(self, padre, hijos, profundidad, esUltimo=False):
        lineas = [self.obtenerCadenaDelNodo(padre.valor, profundidad, esUltimo)]
        for hijo in hijos:
            esUltimoHijo = hijo is hijos[-1]
            lineas.extend(self.imprimirRecursivo(hijo, hijo.hijos, profundidad+1, esUltimoHijo))
        return lineas
    


    def obtenerCadenaDelNodo(self, valor, profundidad, esUltimo):
        if profundidad == 0:
            return str(valor)
        return f"{'│  ' * (profundidad-1)}{'└─ ' if esUltimo else '├─ '}{valor}"




