#Faça um Programa que leia três números e mostre o maior deles.
n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número: '))
n3 = int(input('Digite mais um número: '))
maior = n1
if n2 > maior:
    maior = n2
elif n3 > maior:
    maior = n3
print(f'{maior} é o maior número digitado.')