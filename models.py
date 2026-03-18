class Persona():
    def __init__(self, idPersona, nombre, email):
        self.idPersona = idPersona
        self.nombre = nombre
        self.email = email
    def login(self):
        return f"Bienvenid@ {self.nombre}"
    def actualizarDatos (self, nuevoEmail):
        self.email= nuevoEmail
        return f"{self.nombre} tus datos han sido actualizados .Nuevo email: {self.email}"
class Usuario(Persona):
    def __init__(self, idPersona, nombre, email, limitePrestamos): #las listas no van como parametro
        super().__init__(idPersona, nombre, email)
        self.limitePrestamos = limitePrestamos
        self.listaActiva = []#lista vacia
    def agregarPrestamo(self, prestamo):
        if len(self.listaActiva) < self.limitePrestamos:
            self.listaActiva.append(prestamo)
            return f"Préstamo agregado. Actualmente tienes {len(self.listaActiva)} préstamos activos."
        else:
            return f"No puedes agregar más préstamos. Has alcanzado el límite de {self.limitePrestamos} préstamos activos."
class Bibliotecario(Persona):
    def __init__(self, idPersona, nombre, email):
        super().__init__(idPersona, nombre, email)
    def gestionarPrestamo(self, prestamo):
        return f"El bibliotecario {self.nombre} esta gestionando el prestamo: {prestamo.idPrestamo}"
    def transferirMaterial(self, material, sucursalDestino):
        return f" El material {material.titulo} ha sido transferido a la sucursal: {sucursalDestino.nombre} "
class Material():
    def __init__(self, idMaterial, titulo, anoPublicacion):
        self.idMaterial = idMaterial
        self.titulo = titulo
        self.anoPublicacion = anoPublicacion
        self.disponible = True
    def verificarDisponibilidad(self):
        if self.disponible:
            return f"El material {self.titulo} está disponible"
        else:
            return f"El material: '{self.titulo}' no esta disponible"
    def cambiarDisponibilidad(self):
        self.disponible = not self.disponible 
        return f"Disponibilidad de '{self.titulo}' cambia a {self.disponible}"
    def obtenerInformacion(self):
       return f"Material: {self.titulo} | Año: {self.anoPublicacion} | Disponible: {self.disponible}"
class Libro(Material):
    def __init__(self, idMaterial, titulo, anoPublicacion, autor, isbn, genero):
        super().__init__(idMaterial, titulo, anoPublicacion)
        self.autor = autor
        self.isbn = isbn
        self.genero = genero
class Revista(Material):
    def __init__(self, idMaterial, titulo, anoPublicacion, edicion, tiempoPublicacion):
        super().__init__(idMaterial, titulo, anoPublicacion)
        self.edicion = edicion
        self.tiempoPublicacion = tiempoPublicacion
class MaterialDigital(Material):
    def __init__(self, idMaterial, titulo, anoPublicacion, tipoArchivo, urlDescarga, tamanoMB):
        super().__init__(idMaterial, titulo, anoPublicacion)
        self.tipoArchivo = tipoArchivo
        self.urlDescarga = urlDescarga
        self.tamanoMB = tamanoMB
class Prestamo():
    def __init__(self, idPrestamo, fechaInicio, fechaDevolucion, usuario, material):
        self.idPrestamo = idPrestamo
        self.fechaInicio = fechaInicio
        self.fechaDevolucion = fechaDevolucion
        self.usuario = usuario
        self.material = material
    def obtenerDetalle(self):
        return f"El material {self.material.titulo} al usuario: {self.usuario.nombre}. Fue prestado desde: {self.fechaInicio} y la fecha de devolucion es: {self.fechaDevolucion}. Id del prestamo: {self.idPrestamo}"
class Penalizacion():
    def __init__(self, monto, motivo): 
        self.monto = monto
        self.motivo = motivo
        self.pagada = False #inicia en false 
    def calcularMulta(self, diasRetraso, usuario):
        self.precioFinal = diasRetraso*self.monto
        return f"La multa del usuario {usuario.nombre} es: ${self.precioFinal}"
    def bloquearUsuario(self, usuario):
        return f"El usuario: {usuario.nombre} fue bloqueado por {self.motivo}"   
class Sucursal():
    def __init__(self, idSucursal, nombre):
        self.idSucursal = idSucursal
        self.nombre = nombre
        self.catalogoLocal = []
    def agregarMaterial(self, material):
        self.catalogoLocal.append(material)
        return f"Material '{material.titulo}' agregado a sucursal {self.nombre}"
class Catalogo():
    def __init__(self, materiales):
        self.materiales = materiales
    def buscarPorAutor(self, autor):
        resultados = [m for m in self.materiales if isinstance(m, Libro) and m.autor == autor]
        return f"Libros de {autor}: {[m.titulo for m in resultados]}"
    def buscarEnTodasSucursales(self, titulo):
        resultados = [m for m in self.materiales if m.titulo == titulo]  
        return f"Resultados para '{titulo}': {[m.titulo for m in resultados]}"

    

           