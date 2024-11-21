dias= ["lunes", "martes","miercoles","jueves","viernes","sabado","domingo"]

print(dias)
print(dias[0])
print(dias[1:5])
print(len(dias))


gravedad_planetas= [12.98 ,124.5, 154 , 89.3]
pesso_bus= 214243 #newtons en la tierra

print(f"el peso del bus en la tierra es {pesso_bus} N")
print(f"el peso del bus en dia lusnes pesa {pesso_bus* gravedad_planetas[1]} N")

print(f"la gravedad menos liviad es: {min(gravedad_planetas)}")
print(f"la gravedad mas pesada es: {max(gravedad_planetas)}")