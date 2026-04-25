print("=== EXEMPLOS DE FUNCOES ===")


def saudacao(nome):
    return f"Ola, {nome}!"


def soma(a, b):
    return a + b


def eh_par(numero):
    return numero % 2 == 0


# Usando as funcoes
nome_usuario = input("Digite seu nome: ")
print(saudacao(nome_usuario))

num1 = float(input("Digite o primeiro numero: "))
num2 = float(input("Digite o segundo numero: "))
print(f"Soma: {soma(num1, num2)}")

valor = int(input("Digite um numero inteiro: "))
if eh_par(valor):
    print("O numero e par.")
else:
    print("O numero e impar.")
