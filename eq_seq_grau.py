import math

def eq (a,b,c):
    delta = (b ** 2) / (4 * a * c)
    delta_positivo = (-b + (delta ** 0.5)) / 2 * a
    delta_negativo = (-b + (- delta ** 0.5)) / 2 * a
    return delta_positivo,delta_negativo

a = float(input('Qual o valor de A?:'))
b = float(input('Qual o valor de B?:'))
c = float(input('Qual o valor de C?:'))

resultado = eq(a,b,c)
print(f"Os resultados foram: {resultado[0]} e {resultado[1]}")
