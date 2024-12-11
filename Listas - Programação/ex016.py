# Utilize uma lista para resolver o problema a seguir. 
# Uma empresa paga seus vendedores com base em comissões.
# O vendedor recebe $200 por semana mais 9 por cento de suas vendas brutas daquela semana. 
# Por exemplo, um vendedor que teve vendas brutas de $3000 em uma semana recebe $200 mais 9 por cento de $3000, 
# ou seja, um total de $470. 
# Escreva um programa (usando um array de contadores) 
# que determine quantos vendedores receberam salários nos seguintes intervalos de valores: 
#a. $200 - $299 
#b. $300 - $399 
#c. $400 - $499 
#d. $500 - $599 
#e. $600 - $699 
#f. $700 - $799 
#g. $800 - $899 
#h. $900 - $999 
#i. $1000 em diante 

import numpy as np

sal = []
contadores = np.zeros(9) 
vendaBruta = 0
quant = int(input('Digite quantos funcionário tem: '))

for i in range (quant):
    vendaBruta = float(input(f'Digite quanto de vendas brutas o {i+1}º vendedor teve: '))
    sal.append(200 + vendaBruta * 0.09)
    if sal[i] >= 200 and sal[i] <= 299:
        contadores[0] += 1
    elif sal[i] >= 300 and sal[i] <= 399:
        contadores[1] += 1
    elif sal[i] >= 400 and sal[i] <= 499:
        contadores[2] += 1
    elif sal[i] >= 500 and sal[i] <= 599:
        contadores[3] += 1
    elif sal[i] >= 600 and sal[i] <= 699:
        contadores[4] += 1
    elif sal[i] >= 700 and sal[i] <= 799:
        contadores[5] += 1
    elif sal[i] >= 800 and sal[i] <= 899:
        contadores[6] += 1
    elif sal[i] >= 900 and sal[i] <= 999:
        contadores[7] += 1
    elif sal[i] >= 1000:
        contadores[8] += 1 
        
print('Existem:')
v = 200
v1 = 299
for i in range (9):
    print(f'{contadores[i]} funcionário(s) que ganham de {v} a {v1}.')
    v += 100
    v1 += 100