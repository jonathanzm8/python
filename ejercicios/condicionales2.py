import random

aleatorio=random.randint(1,9)
aleatorio2=random.randint(1,9)

if aleatorio==1:
    print("te ganaste un celular")

elif aleatorio==7:
    print("te ganaste un balon")

elif aleatorio==9 and aleatorio2==2:
    print("te ganaste unos zapatos")

else:
    print("perdiste!!!")