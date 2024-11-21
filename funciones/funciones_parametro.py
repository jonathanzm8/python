def datos(nombre, apellido, edad, mesaje):
    if edad< 18:
        print(f"{mesaje} {nombre} {apellido} {edad}  es menor de edad" )
    else:
        print(f"{mesaje} {nombre} {apellido} {edad}  es mayor de eda" )