
# ecuador 


import random
velocidad= random.randint(10,91)

#zona urbana max 50km/h  min10km/h
if velocidad<=10 or velocidad<=50:
    print("ZONA URBANA")
    print("respetando los limites de velocidad")
else:
    print("ZONA URBANA")
    print("infrigiendo los limites de velocidad")

#zona rural max 70km/h  min51km/h

if velocidad<=70 or velocidad<=51:
    print("ZONA RURAL")
    print("respetando los limites de velocidad")
else:
    print("ZONA RURAL")
    print("infrigiendo los limites de velocidad")

#zona perimetral max 90km/h  min71km/h

if velocidad<=90 or velocidad<=71:
    print("ZONA PERIMETRAL")
    print("respetando los limites de velocidad")
else:
    print("ZONA PERIMETRAL")
    print("infrigiendo los limites de velocidad")
