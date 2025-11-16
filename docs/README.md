<h1>Cliente de Correo Electrónico</h1>

Este proyecto implementa un cliente de correo electrónico orientado a objetos en Python. Permite gestionar usuarios, mensajes, carpetas y operaciones típicas de un entorno de email, como envío, recepción, organización jerárquica y navegación.

<h1>Estructura del proyecto</h1>



 - main.py : 	Punto de entrada del sistema

- sistemaEmail.py :	Orquestador principal: gestiona usuarios, sesiones y operaciones

- usuario.py :	Modelo de usuario con bandeja de carpetas y autenticación
- mensaje.py :	Define los mensajes con asunto, cuerpo, remitente, etc.
- carpeta.py :	Contenedor de mensajes
- arbolCarpetas.py :	Estructura recursiva de carpetas
- servidorCorreo.py :	Agrupa usuarios por servidor
- interfazDeUsuario.py :	Presentación textual del sistema
- herramientas.py :	Utilidades como encriptación y validación

<h2>Clases principales y metodos</h2>

- Sistema Email


  - servidores: ServidorCorreo[]

  - usuarioAutenticado: Usuario

  - iniciarSesion(correo: string, clave: string):
  - registrar(nombre: string, correo: string,  
  contraseña: string, validarContraseña: string)
  - cerrarSesion()
  - enviarMensaje(correoDestinatario: string, asunto: string,  
   cuerpo: string, prioridad: number)
  - crearNuevaCarpeta()
  - verBanedeja()
  - \_\_encontrarUsuarioEnLosServidores(correo: string): Usuario

  - \_\_retornarServidorMenosLleno(): ServidorCorreo

---

- ServidorCorreo

  - nombreServicio: string
  - usuarios: Usuario[]
  - buscarUsuario(nombre: string): Usuario
  - agregarUsuarioAlServidor(usuario: Usuario):
  - buscarUsuarioPorEmail(email: string): Usuario

---

- Usuario

  - nombre: string
  - correo: string
  - \_\_clave: string
  - bandeja: Carpeta

  - authenticarse(correo: string, clave: string)
  - agregarMensaje(mensaje: Mensaje)
  - agregarMensajeEnviado(mensaje: Mensaje)
  - verContenidoBandeja()
  - verCarpetas()
  - listarMensajePrioridad()
  - agregarNuevaCarpeta(nombreCarpetaPadre:string, nombreNuevaCarpetaHija:string)
  - \_\_hashClave()

---

- Mensaje

  - asunto: string
  - cuerpo: string
  - remitente: string
  - destinatario: string
  - prioridad: number

    **str**(): string

---

- Carpeta

  - nombre: string
  - subcarpetas: Carpeta[]
  - mensajes: Mensaje[]

  - crearSubcarpetas(nombre:string)
  - agregarMensaje(mensaje:Mensaje)
  - listarMensajesDeCarpeta()
  - listarCarpetas()

---

---

<h2>Encapsulamiento</h2>

Todos los atributos importantes son privados (__atributo) y se accede mediante métodos o propiedades. Esto protege la información y evita accesos directos no deseados.

<h2>Roles claros por clase</h2>

- Usuario: gestiona sus carpetas y mensajes.

- Mensaje: encapsula la información del correo.

- Carpeta: organiza los mensajes y subcarpetas.

- ServidorCorreo: conecta usuarios y permite buscarlos.

- SistemaEmail: orquesta todo el funcionamiento del sistema.

<h2>Extensibilidad y reutilización</h2>

- El sistema puede crecer fácilmente: filtros, etiquetas, búsquedas por prioridad, reglas de clasificación.

- Los métodos como listar() se reutilizan en múltiples contextos, lo que hace que el diseño sea flexible y adaptable.

<h2> Recursividad en la gestión de carpetas</h2>

El sistema implementa una estructura jerárquica de carpetas mediante la clase `ArbolCarpetas`, que permite insertar, buscar y recorrer carpetas de forma recursiva.

La navegación por carpetas se realiza con el método `_obtenerMensajeNavegando()` en `SistemaEmail`, que permite al usuario:

- Ingresar a subcarpetas sin límite de profundidad
- Retroceder a carpetas superiores
- Seleccionar mensajes dentro de cualquier carpeta del árbol

Esto garantiza que las operaciones de movimiento y selección de mensajes no se limitan al primer nivel, sino que recorren todo el árbol de carpetas de forma dinámica y recursiva.

<h2>Análisis de eficiencia algorítmica</h2>

El sistema utiliza estructuras simples y eficientes para garantizar una navegación fluida y operaciones rápidas:

- **Búsqueda de usuario por correo**  
  Se recorre la lista de servidores y sus usuarios hasta encontrar coincidencia.  
  Complejidad: O(n), donde n es la cantidad total de usuarios en todos los servidores.

- **Navegación por árbol de carpetas**  
  El árbol permite recorrer carpetas y subcarpetas sin límite de profundidad.  
  Complejidad: O(d), donde d es la profundidad del árbol.

- **Movimiento de mensajes entre carpetas**  
  Se busca la carpeta destino y se elimina/agrega el mensaje.  
  Complejidad: O(m), donde m es la cantidad de carpetas recorridas hasta encontrar la carpeta destino.

- **Envío de mensajes**  
  Se agrega el mensaje al remitente y al destinatario.  
  Complejidad: O(1), ya que se accede directamente a las carpetas “Enviados” y “Bandeja de entrada”.

<h2>Manejo de casos límite</h2>

El sistema contempla distintos escenarios de error y situaciones límite para garantizar una experiencia robusta:

- **Carpeta inexistente**  
  Si el usuario intenta mover un mensaje a una carpeta que no existe, el sistema detecta el error y muestra un mensaje informando que la operación no se puede realizar.

- **Mensaje no encontrado**  
  Durante la navegación por carpetas, si el usuario selecciona un índice inválido o un mensaje que no existe, se muestra una advertencia y se permite continuar naveg

Estas operaciones están diseñadas para mantener la eficiencia incluso cuando el sistema escala en cantidad de usuarios y carpetas.

<h2>Pruebas unitarias (recomendación)</h2>

Aunque no se incluyen en esta entrega, se recomienda implementar pruebas unitarias para verificar el correcto funcionamiento de los componentes principales del sistema.

Las pruebas sugeridas incluyen:

- **Inserción y búsqueda de carpetas**  
  Validar que el árbol de carpetas permite agregar y encontrar carpetas en cualquier nivel.

- **Envío y recepción de mensajes**  
  Verificar que los mensajes se agregan correctamente a las carpetas “Enviados” y “Bandeja de entrada”.

- **Movimiento de mensajes entre carpetas**  
  Confirmar que los mensajes se eliminan de la carpeta origen y se agregan a la carpeta destino.

- **Autenticación de usuarios**  
  Probar que la validación de claves funciona correctamente y que no se permite acceso con credenciales incorrectas.

Estas pruebas pueden implementarse utilizando unittest o pytest, y permitirían validar automáticamente el comportamiento del sistema ante cambios o ampliaciones futuras.




<h2>Orquestador central</h2>

Utilizamos una clase principal llamada `SistemaEmail` para coordinar todos los elementos del sistema: usuarios, envío de mensajes, creación y login de usuarios, navegación por carpetas, etc

<h2>Diagrama de clases</h2>

![](https://github.com/fernandofunez/TpUnab/blob/786d6a44a25f76f0cf381f015518ac7fdb293324/docs/DiagramaDeClases.PNG)




<br>
<br>
<br>


<h2>Integrantes y entrega</h2>

**Autor**: Bacelar Federico - Quevedo Matias - Funez Fernando  
**Materia**: estructura de Datos  
**Profesor**: Bianco, Leonardo Angel  
**Entrega**:   15 - 11 - 2025
** Grupo ** : 27
