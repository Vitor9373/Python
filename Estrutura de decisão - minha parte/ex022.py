#Faça um Programa que peça um número inteiro e determine se ele é par ou ímpar. 
# Dica: utilize o operador módulo (resto da divisão).

x = int(input('Digite um número inteiro: '))

if x % 2 == 0:
    print('O número é par.')
else:
    print('O número é ímpar.')  