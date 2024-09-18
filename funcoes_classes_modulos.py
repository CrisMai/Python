
import math

print(math.sqrt(16))  # Saída: 4.0
print(math.pow(2, 3))  # Saída: 8.0
print(math.pi)  # Saída: 3.141592653589793


# ----------------------------

import random

print(random.random())  # Saída: Um número aleatório entre 0 e 1
print(random.randint(1, 10))  # Saída: Um número aleatório entre 1 e 10
lista = [1, 2, 3, 4, 5]
random.shuffle(lista)
print(lista)  # Saída: A lista embaralhada


# --------------------------------

import datetime

# Data e hora atuais
agora = datetime.datetime.now()
print(agora)  # Exibe a data e hora atual

# Trabalhando com datas
hoje = datetime.date.today()
print(hoje)  # Exibe a data atual
