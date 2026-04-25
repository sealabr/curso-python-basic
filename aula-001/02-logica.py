print("=== EXEMPLOS DE LOGICA ===")

# 1) Verificar se um numero e par ou impar
numero = int(input("Digite um numero inteiro: "))
if numero % 2 == 0:
    print("O numero e par.")
else:
    print("O numero e impar.")

# 2) Comparar dois numeros
valor1 = float(input("Digite o primeiro valor: "))
valor2 = float(input("Digite o segundo valor: "))

if valor1 > valor2:
    print("O primeiro valor e maior.")
elif valor2 > valor1:
    print("O segundo valor e maior.")
else:
    print("Os valores sao iguais.")

# 3) Verificar faixa de nota
nota = float(input("Digite uma nota de 0 a 10: "))
if nota >= 7:
    print("Aprovado.")
elif nota >= 5:
    print("Recuperacao.")
else:
    print("Reprovado.")
