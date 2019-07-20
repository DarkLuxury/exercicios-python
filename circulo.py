def comp (raio):
    comprimento = 2 * raio * 3.14
    return comprimento

def ar (raio):
    area = 3.14 * (raio ** 2)
    return area

raio = float(input("Qual o raio?: "))
print(f"O comprimento desta circunferência é de: {comp(raio)} e a área é de: {ar(raio)}")