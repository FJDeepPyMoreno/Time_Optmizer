import numpy as np
from datetime import datetime
"""
En este programa vamos a generar secuencias de números aleatorios y determinaremos el 
periodo de las mismas.

"""

# Comenzamos por secuencias cortas:
np.random.seed(1)
a = np.random.randint(0, 10, 6000)
# print(a)
b = a[:3]
print(b)
t0 = datetime.now()
coincidencia = False
for x in range(1,len(a)-len(b)):
 #    print(a[x:x+len(b)])
     if np.array_equal(b,a[x:x+len(b)]):
         coincidencia = True
         x_coincidencia = x
         break

if coincidencia:
    print("Coincidencia en posición: ", x_coincidencia)
else:
    print("No hay coincidencia")

t1 = datetime.now()
print("Tiempo total: ", t1-t0)
