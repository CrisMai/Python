
# 39.0 - Cálculo do IMC

nome = 'Cris'
altura = 1.63
peso = 49
imc = peso / (altura * altura)
print(nome, 'tem', altura, 'de altura')
print('pesa', peso, 'quilos e seu IMC é')
print(imc)


# Outra forma de resolver

nome = 'Cris'
altura = 1.63
peso = 49
imc = peso / (altura ** 2)
print(imc)


# Usando f-strings

nome = 'Cris'
altura = 1.63
peso = 49
imc = peso / (altura * altura)

linha_1 = f'{nome} tem {altura:.2f} de altura'
linha_2 = f'pesa {peso} quilos e seu IMC é'
linha_3 = f'{imc:.2f}'

print(linha_1)
print(linha_2)
print(linha_3)

