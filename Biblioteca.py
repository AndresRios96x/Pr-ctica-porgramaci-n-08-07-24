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
        
     
        
        
        