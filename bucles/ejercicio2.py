datos= []

ingresar= input("ingrese el dato: ")


datos.append(ingresar)

for i in datos:
    if ingresar.isdigit():# validacion si es digito
        print(f"la cadena es de digitos: {datos}")
    elif str(ingresar): # validacion si es estring
        print(f"la cadena es estring: {datos}")


print(f"Su lista es: {datos}")