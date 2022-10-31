class Jugador:
    def __init__(self,nombre,apellido,seleccion,region,numero,imagen):
        self.nombre = nombre
        self.apellido = apellido
        self.seleccion = seleccion
        self.region = region
        self.numero = numero
        self.imagen = imagen
    
    
    def getNombre(self):
        return self.nombre
    
    def getApellido(self):
        return self.apellido
    
    def getSeleccion(self):
        return self.seleccion
    
    def getRegion(self):
        return self.region
    
    def getNumero(self):
        return self.numero
    
    def getImagen(self):
        return self.imagen