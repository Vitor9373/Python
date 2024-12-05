#Faça um Programa que leia 2 números e em seguida pergunte ao usuário qual operação ele deseja realizar.
#O resultado da operação deve ser acompanhado de uma frase que diga se o número é:
#par ou ímpar;
#positivo ou negativo;
#inteiro ou decimal.

n1 = float(input('Informe n1: '))
n2 = float(input('Informe n2: '))
op = input('Informe a operacao(+-*/): ')
res = 0

if op == '+':
    res = n1 + n2
elif op == '-':
    res = n1 - n2
elif op == '*':
    res = n1 * n2
elif op == '/':
    res = n1 / n2
    
if res % 2 == 0:
    pi = 'Par'
else:
    pi = 'ímpar'
if res > 0:
    pn = 'Positivo'
else:
    pn = 'Negativo'
if res.is_integer():
    id = 'inteiro'
else:
    id = 'Decimal'

print(f'O resultado da operação é {res};\nSendo o número {pi}, {pn} e {id}.')