class Auto:
    def __init__(self, marca, modelo, año, kilometraje=0):
        self.marca = marca
        self.modelo = modelo
        self.año = año
        self.kilometraje = kilometraje
    
    def mostrar_informacion(self):
        return f"Marca: {self.marca}, Modelo: {self.modelo}, Año: {self.año}, Kilometraje: {self.kilometraje}"
    
    def actualizar_kilometraje(self, kilometrajenuevo):
        self.kilometraje = kilometrajenuevo
        return self.kilometraje
        
    def realizar_viaje(self, kilometros_recorridos):
        self.kilometraje += kilometros_recorridos
        return self.kilometraje
    
    def estado_auto(self):
        if self.kilometraje < 20000:
            print("Estoy como nuevo")
        elif 20000 <= self.kilometraje <= 100000:
            print("Ya estoy usado")
        else:
            print("¡Ya déjame descansar por favor!")
        return self.kilometraje


informacion = Auto("Hyundai", "Tucson", 2007)

print(informacion.mostrar_informacion())

print(f"El nuevo kilometraje es: {informacion.actualizar_kilometraje(100)}")

print(f"El kilometraje después del viaje es: {informacion.realizar_viaje(100000)}")

print(f"Estado del auto: {informacion.estado_auto()}")