from ejercicio import Auto

año_auto= Auto.auto_año("corsa")

auto1=Auto("Hyundai", "Tucson", 2007, 50)
auto2=Auto("Hyundai", "Tucson", 2007, 50)

kilometraje= Auto.validar_kilometraje(auto1,auto2)

print(kilometraje)

print(año_auto.__dict__)

