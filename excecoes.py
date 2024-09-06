
# Try

try:
    x = 10 / 0  # Tenta dividir por zero
except ZeroDivisionError:
    print("Erro: Não é possível dividir por zero.")


# Else

try:
    x = 10 / 2
except ZeroDivisionError:
    print("Erro: Não é possível dividir por zero.")
else:
    print("Divisão realizada com sucesso. Resultado:", x)


# Finally

try:
    x = 10 / 0
except ZeroDivisionError:
    print("Erro: Não é possível dividir por zero.")
finally:
    print("Bloco finally executado, encerrando operação.")



# Vamos ver um exemplo completo que usa try, except, else, e finally:

def ler_numero():
    try:
        numero = int(input("Digite um número: "))
    except ValueError:
        print("Erro: Você não digitou um número válido.")
    else:
        print(f"Você digitou o número: {numero}")
    finally:
        print("Operação finalizada.")

# Executando a função
ler_numero()