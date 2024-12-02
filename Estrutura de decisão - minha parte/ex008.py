#Faça um programa que pergunte o preço de três produtos e informe qual produto você deve comprar,
#sabendo que a decisão é sempre pelo mais barato.
n1 = int(input('Digite o primeiro preço: '))
n2 = int(input('Digite o segundo preço: '))
n3 = int(input('Digite o terceiro preço: '))
menor = n1
if n2 < menor:
    menor = n2
elif n3 < menor:
    menor = n3
print(f'{menor} é o menor preço.')