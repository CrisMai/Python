
frutas = {"maçã", "banana", "laranja"}


frutas.add("pera")
print(frutas)  # Imprime {"maçã", "banana", "laranja", "pera"}

frutas.remove("banana")
print(frutas)  # Imprime {"maçã", "laranja", "pera"}

frutas.discard("uva")
print(frutas)  # Imprime {"maçã", "laranja", "pera"}

frutas.clear()
print(frutas)  # Imprime set()


conjunto = {1, 2, 3}


elemento = conjunto.pop()  # Remove e retorna um elemento arbitrário

conjunto1 = {1, 2, 3}
conjunto2 = {3, 4, 5}
uniao = conjunto1.union(conjunto2)  # uniao é {1, 2, 3, 4, 5}

conjunto1 = {1, 2, 3}
conjunto2 = {2, 3, 4}
interseccao = conjunto1.intersection(conjunto2)  # interseccao é {2, 3}

conjunto1 = {1, 2, 3}
conjunto2 = {2, 3, 4}
diferenca = conjunto1.difference(conjunto2)  # diferenca é {1}