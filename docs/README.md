SistemaDeEmail

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

* \_\_retornarServidorMenosLleno(): ServidorCorreo

---

ServidorCorreo

- nombreServicio: string
- usuarios: Usuario[]
- buscarUsuario(nombre: string): Usuario
- agregarUsuarioAlServidor(usuario: Usuario):
- buscarUsuarioPorEmail(email: string): Usuario

---

Usuario

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

Mensaje

- asunto: string
- cuerpo: string
- remitente: string
- destinatario: string
- prioridad: number

**str**(): string

---

Carpeta

- nombre: string
- subcarpetas: Carpeta[]
- mensajes: Mensaje[]

- crearSubcarpetas(nombre:string)
- agregarMensaje(mensaje:Mensaje)
- listarMensajesDeCarpeta()
- listarCarpetas()

---

---

Encapsulamiento: Todos los atributos importantes son privados (\_\_atributo) y se accede mediante métodos o propiedades. Esto protege la información y evita accesos directos no deseados.

Roles claros por clase:

- Usuario gestiona sus carpetas y mensajes.

- Mensaje encapsula la información del correo (asunto, cuerpo, remitente, destinatario, prioridad).

- Carpeta organiza los mensajes y subcarpetas.

- ServidorCorreo conecta usuarios y permite buscarlos por nombre o correo.

- SistemaEmail coordina todo el funcionamiento del sistema.

Extensibilidad: El sistema puede crecer fácilmente. Se pueden agregar filtros, etiquetas, búsquedas por prioridad, reglas de clasificación, etc.

Reutilización: Los métodos como listar() pueden usarse en múltiples contextos (carpetas, mensajes, usuarios), lo que hace que el diseño sea flexible y adaptable.

Orquestador central: Utilizamos una clase central/padre llamada "SistemaEmail" para orquestar todos los demás objetos.
#Orquestador de los ELEMENTOS de la aplicación
#NO ES EL ARRANQUE. Es el orquestador → Maneja: usuarios, envío de mensajes, creación/logueo de usuarios, etc.
