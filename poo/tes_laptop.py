from laptop import Laptop

laptop1= Laptop("asus","i7",16)

print(laptop1.__dict__)

laptop_business= Laptop.realizar_diagnostico_sistema(laptop1)

print(laptop_business)