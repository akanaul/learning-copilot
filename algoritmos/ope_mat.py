# Solicitar como entrada dois numeros inteiros e realizar as quatro operacoes matematicas basicas com base no operador escolhido pelo usuario


num1 = int(input("Digite o primeiro número inteiro: "))
num2 = int(input("Digite o segundo número inteiro: "))

operacao = input("Escolha a operação (+, -, *, /): ")

# Realizar a operação escolhida
if operacao == '+':
    resultado = num1 + num2
elif operacao == '-':
    resultado = num1 - num2
elif operacao == '*':
    resultado = num1 * num2
elif operacao == '/':
    resultado = num1 / num2 if num2 != 0 else "Divisão por zero não é permitida"
else:
    resultado = "Operação inválida"

print("O resultado é:", resultado)
