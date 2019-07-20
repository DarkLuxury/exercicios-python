import random

numeros_aleatorios = [random.randint(1,100),random.randint(1,100),random.randint(1,100),random.randint(1,100),random.randint(1,100),
                      random.randint(1,100),random.randint(1,100),random.randint(1,100),random.randint(1,100),random.randint(1,100)]

i = 0
pares = []
impares = []

while i < len(numeros_aleatorios):
    if numeros_aleatorios[i] % 2 == 0:
        pares.append(numeros_aleatorios[i])
    else:
        impares.append(numeros_aleatorios[i])
    i = i + 1

print(pares)
print(impares)