nombre_paciente= []
edad= []

def agregar_nombres(nombres):
    nombre_paciente.append(nombres)
    print(f"NOMBRES: {nombre_paciente}")

def agregar_edad(año_nacimiento):
    edad_actual= 2024 -año_nacimiento
    edad.append(edad_actual)
    
    # if edad_actual> 18:
    #     print(f"es mayor de edad {nombre_paciente}")
    # elif edad_actual<18:
    #     print(f"es menor de edad {nombre_paciente} ")
    # else:
    #     print("palo")
    print(f"EDADES: {edad}")

