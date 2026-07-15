# --- Snippet 1 ---
# PREDIGO:

# ["b", "c", "d"]
# ["d", "e"]
# ["e", "d", "c", "b", "a"]

letras = ["a", "b", "c", "d", "e"]
print(letras[1:4])
print(letras[-2:])
print(letras[::2])

# REAL:

# ['b', 'c', 'd']
# ['d', 'e']
# ['a', 'c', 'e']

# LECCIÓN: el slice tiene tres ranuras [start:stop:step]

# --- Snippet 2 ---
# PREDIGO:

# Error

datos = [0, 1, "", "test", None, [], "QA"]
limpios = [d for d in datos if d]
print(limpios)

# REAL:

# [1, 'test', 'QA']


# LECCIÓN: la condicion evalua los truthy

# --- Snippet 3 ---
# PREDIGO:

# true
# true
# no se encuentra timeout

config = {"browser": "chrome", "headless": True}
print("chrome" in config)
print("browser" in config)
print(config.get("timeout", 30))

# REAL:

# False
# True
# 30


# LECCIÓN: el primero da false porque porqie in en un diccionario busca claves, no valores ( a menos que lo especifiquemos). En cuanto al get, como no encuentra timeout devuelve 30 que es el default

# --- Snippet 4 ---
# PREDIGO:

# 7, 0

ids = [3, 1, 2, 3, 1, 2, 3]
unicos = set(ids)
print(len(ids), len(unicos))

# REAL: 

# 7 3

# LECCIÓN: Cada valor aparece una vez, sin importar cuántas veces vino.

# --- Snippet 5 ---
# PREDIGO:

# Error, esto no es una lista, no podemos modificar/acceder por indice.

punto = (10, 20)
punto[0] = 99
print(punto)

# REAL:

# TypeError: 'tuple' object does not support item assignment
# Las tuples son secuencias (igual que strings y listas): indexables, sliceables, iterables. Lo único que no soportan es item assignment


# LECCIÓN: no podemos modificar una tupla, son inmutables

