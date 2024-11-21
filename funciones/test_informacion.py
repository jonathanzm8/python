import informacion

nombres = int(input("ingrese el numero de pacientes: "))
mayores= []
menores=[]

for i in range(nombres):

    nombre= input("ingrese su nombre y apellido: ")
    
    año_nacimento= int(input("ingrese el año de nacimenito: "))

    edad_actual= 2024 -año_nacimento

    if edad_actual> 18:
        mayores.append(nombre)
        print(f"pacientes mayores de edad: {mayores}")
    elif edad_actual<18:
         menores.append(nombre)
         print(f"pacientes menores de edad: {menores}")
    informacion.agregar_nombres(nombre)
    informacion.agregar_edad(año_nacimento)