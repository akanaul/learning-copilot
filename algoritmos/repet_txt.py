# Solicitar uma string e um numero inteiro do usuario e repetir a string i vezes

texto = input("Digite uma string: ")
num = int(input("Digite um número inteiro: "))

resultado = ' '.join([texto] * num)

print("O resultado é:", resultado)