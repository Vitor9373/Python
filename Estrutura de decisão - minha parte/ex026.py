#Um posto está vendendo combustíveis com a seguinte tabela de descontos:
#Álcool:
#    até 20 litros, desconto de 3% por litro
#    acima de 20 litros, desconto de 5% por litro
#Gasolina:
#     até 20 litros, desconto de 4% por litro
#     acima de 20 litros, desconto de 6% por litro 
#Escreva um algoritmo que leia o número de litros vendidos, 
# o tipo de combustível (codificado da seguinte forma: A-álcool, G-gasolina), 
# calcule e imprima o valor a ser pago pelo cliente 
# sabendo-se que o preço do litro da gasolina é R$ 2,50 o preço do litro do álcool é R$ 1,90.

c = input('Digite qual combustível deseja usar (A-álcool, G-gasolina):').upper()
l = float(input('Quantos litros deseja abastecer?:'))
pa = l * 1.9
pg = l * 2.5
p = 0

if c == 'A':
    if l > 20:
        pa = pa * 0.95
    else:
        pa = pa * 0.97
    p = pa
elif c == 'G':
    if l > 20:
        pg = pg * 0.94
    else:
        pg = pg * 0.96
    p = pg
else:
    print('Tipo inválido!')
    
print(f'Você irá pagar {p} reais.')