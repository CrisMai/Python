
def calcular_media(*numeros):
    soma = sum(numeros)
    quantidade = len(numeros)
    media = soma / quantidade
    return media

print("Media:", calcular_media(10, 20, 30,40))

# Função lambda

def somar_3(x):
    return x + 3

somar = lambda x: x + 3

print("Somar 3 a um numero:", somar(8))
