class Libro: 
    def _init_ (self, titulo, autor, ejemplares):
        self.titulo = titulo 
        self.autor = autor
        self.ejemplares = ejemplares 
        self.prestados = 0 
        
    def disponibles(self):
        return self.ejemplares - self.prestados
    
    def prestar(self): 
        if self.disponibles() > 0:
            self.prestados += 1 
            print(f"Has tomado prestado el libro '{self.titulo}' del autor '{self.autor}'")
            return True
        else: 
            print("lo siento, no hay ejemplares disponibles de '{self.titulo}' en este momento")
            return False
        
    def devolver(self): 
        if self.prestados > 0:
            self.prestados -= 1
            print(f"Has devuelto el libro '{self.titulo}' del autor '{self.autor}'")
        else:
            print(f"No tienes ejemplares de '{self.titulo}' para devolver")
            
    def __str__(self): 
        return f"'{self.titulo}' de {self.autor} - Disponibles: {self.disponibles()}"
    
    
class Usuario:
    def _init_(self, nombre):
        self.nombre = nombre
        self.librosPrestados = []
        
    def tomarPrestado(self, libro): 
        if libro.prestar():
            self.librosPrestados.append(libro)
            return True 
        else:
            return False
        
    def devolver(self, libro):
        libro.devolver()
        if libro in self.librosPrestados
        self.librosPrestados.remove(libro)
        
    def librosPrestados(self):
        if self.librosPrestados:
            return ", ".join([libro.titulo for libro in self.librosPrestados])
        else: 
            return "Ninguno"
        
    def __str__(self): 
        return f" Usuario:'{self.nombre}' - Libros prestados: {self.librosPrestados()}"
    

class Biblioteca:
    def _init_(self, nombre):
        self.nombre = nombre
        self.catalogo = []
        self.usuarios = []
        
    def agregarLibro(self, libro):
        self.catalogo.append(libro)
        
    def registrarUsuario(self, nombre):
        self.usuarios.append(Usuario(nombre))
    
    def buscarLibro(self, titulo):
        resultados = [libro for libro in self.catalogo if titulo.lower() in libro.titulo.lower()]
        if resultados:
            print(f"Resultados de busqueda para '{titulo}': ")
            for libro in resultados
            print(libro)
        else:
            print(f"No se encontro ningun libro con el titulo: {titulo} en {self.nombre}")
            
    def mostrarCatalogo(self):
        print(f"Caralogo de libros en {self.nombre}: ")
         for libro in self.catalogo
           print(libro)
         print()
    
         
    def mostrarUsuario(self):
        print(f"Usuarios registrados en {self.nombre}: ")
        for usuario in self.usuarios
          print(usuario)  
        print()
        
    def gestionarBiblioteca(self)
        while True:
            print("\nBienvenido a la biblioteca")
            print("1. Agregar libro al catalogo")
            print("2. Registrar un nuevo usuario")
            print("3. Buscar libro por titulo")
            print("4. Mostrar catalogo de libros")
            print("5. Mostrar usuarios registrados")
            print("6. Prestar libro")
            print("7. Devolver libro")
            print("8. Salir")
            
            opcion = input("ingresa la opcion: ")
            
            if opcion == 1:
                titulo = input("Ingrese el titulo del libro: ")
                autor = input("Ingrese el autor del libro: ")
                ejemplares = int(input("Ingrese la cantidad de ejemplares disponibles: "))
                self.agregarLibro(Libro(titulo, autor, ejemplares))
                print(f"El libro '{titulo}' del autor {autor} ha sido agregado al catalogo")
            elif opcion == 2
                 nombreUsuario =  input("Ingrese el nombre del usuario: ")
                 self.registrarUsuario(nombreUsuario)
                 print(f"Usuario: '{nombreUsuario}' registrado exitosamente")
            elif opcion == 3:      
                titulo = input("Ingrese el titulo del libro que desea buscar: ")
                self.buscarLibro(titulo)
            elif opcion == 4 
                self.mostrarCatalogo
            elif opcion == 5
                 self.mostrarUsuario
            elif opcion == 6
                titulo = input("Ingrese el titulo del libro que desea prestar: "
                 libro = next((libro for libro in self.catalogo if libro.titulo.lower() == titulo.lower()), none)
                     
            
        
    
         
        
            
        

        
            
        
        
        
     
        
        
        