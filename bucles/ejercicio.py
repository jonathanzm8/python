frase= input("Ingrese la frase: ")

letra= input("ingrese la letra: ")


contador= 0

for i in frase:
    if i == letra:
        contador +=1
print(f"la letra {letra} se repite {contador}")