from laptop import Laptop
from laptop import laptop_business

laptop1= Laptop("asus","i7",16)

laptop2= laptop_business("dell","i7",32)

# print(laptop1.__dict__)

# laptop_business= Laptop.realizar_diagnostico_sistema(laptop1)

# print(laptop_business)


def imprimir(Laptop):
    informe= Laptop.realizar_informe()
    for clave,valor in informe.items():
        print(f"{clave}, {valor}")
    print(" -----")


print("laptop1")
imprimir(laptop1)

print("laptop2")
imprimir(laptop2)