import random
class Laptop:
    def __init__(self,marca,procesador, memoria, costo=500, impuesto= 10):
        self.marca= marca
        self.procesador= procesador
        self.memoria= memoria
        self.costo= costo
        self.impuesto= impuesto
    def mostrar_informacion(self):
        return f"Marca: {self.marca}, procesador: {self.procesador}, memoria: {self.memoria}, costo: {self.costo}, impusto: {self.impuesto}"

    def __str__(self):
        return f"marca: {self.marca} \n procesador: {self.procesador}\n  memoria: {self.memoria} \n  costo: {self.costo} \n  impuesto: {self.impuesto}"
    
    def valor_final(self):
        return self.costo + self.impuesto
    
    def valor_descuento(self, descuento):
        return (self.costo * descuento)/100
    

    def realizar_diagnostico_sistema(self):
        resultado= {
            "MARCA": f"{self.marca}",
            "PROCESADOR": f"{self.procesador}",
            "MEMORIA_RAM": "ok" if self.memoria >= 8 else "aumentar memmoria ram ",
            "BATERIA": "OK" if random.choice([True,False]) else "cambiar de bateria"
        }
        return resultado
    def realizar_informe(self):
        informe= {
            "tipo": "Generica",
            "Uso recomendado": "tareas cotidianas",
            "horas de uso": "5",
            "diagnostico actual": self.realizar_diagnostico_sistema()
        }
        return informe
    
    @staticmethod
    def compara_costo(lapto1, laptop2):
        if lapto1.costo == laptop2.costo:
            return "los costos son iguales"
        return "los costos son diferentes"
    
    @classmethod
    def asus_latop(cls, costo):
        marca= "asus"
        procesador= "i7"
        memoria= 16
        return cls(marca,procesador, memoria, costo)

    

class laptop_business(Laptop):
    def __init__(self, marca, procesador, memoria, costo=500, impuesto=10):
        super().__init__(marca, procesador, memoria, costo, impuesto)
        
    
    def realizar_diagnostico_sistema(self): # sobre escritura de metodo (tiene la clases laptop este metodo)
        resultado= super().realizar_diagnostico_sistema()
        return resultado
        
    
    def verificar_conectividad(self):
        comprobacion={
            "CONECTIVIDAD": "OK" if random.choice8([True,False]) else "no conectado"
        }
        return comprobacion
    
    def realizar_informe(self):
        informe= {
            "tipo": "laptop bussiness",
            "Uso recomendado": "video juegos",
            "horas de uso": "10",
            "recomedaciones de software": ["antivirus","tarjetaVideo"]
        }
        return informe
    
