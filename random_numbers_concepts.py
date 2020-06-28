import numpy as np

# np.random.rand(N) crea un array de tamaño N con números aleatorios escogidos de la
# distribución uniforme (0,1)

aleatorio = np.random.rand(7)
print(aleatorio)
print(type(aleatorio))

# En lugar de la distribución uniforme, podemos hacer uso de la distribución N(0,1):

aleatorio = np.random.randn(7)
print(aleatorio)
aleatorio = np.random.rand(3,3)
print(aleatorio)
print(type(aleatorio))

# Generación de números enteros aleatorios:

aleatorio = np.random.randint(0,10,15)
# Genera 15 números enteros aleatorios en el intervalo [0,10)
print(aleatorio)

# Podemos darle la forma deseada:

aleatorio = np.random.randint(0,10,size=(4,2))
print(aleatorio)

# Elección aleatoria en los elementos de una lista:

# np.random.choice(.....)

a = np.linspace(0,2,20)
aleatorio = np.random.choice(a,10) # Si 'a' es un array toma elementos de dicho array
print(a)
print(aleatorio)

aleatorio = np.random.choice(11,4) # Toma 4 valores al azar en un array np.arange(11)
print(aleatorio)


# Comprobación de la inicialización de la semilla:
for numero_tandas in range(0,5):
    np.random.seed(1)
    aleatorio = np.random.randint(0,10,6)
    print("Tanda nº {0:d}: ".format(numero_tandas+1), aleatorio)
    # Todas las tandas generadas tienen la misma secuencia.

# Comprobación de la no inicialización sñdlrkgtk
# eokh
# QERKprJPO
# JZde la semilla:
print("\n-----seed = None----- \n")
for numero_tandas in range(0,5):
    np.random.seed(1)
    aleatorio = np.random.randint(0,10,6)
    aleatorio2 = np.random.randint(0,10,6)
    print("Tanda nº {0:d}: ".format(numero_tandas+1), aleatorio)
    print("                ", aleatorio2)

print("\n-----seed = squence----- \n")
np.random.seed(3)
aleatorio = np.random.randint(0,10,6)
aleatorio2 = np.random.randint(0,10,6)
print(aleatorio)
print(aleatorio2)

np.random.seed(3)
aleatorio = np.random.randint(0,10,12)
print(aleatorio)