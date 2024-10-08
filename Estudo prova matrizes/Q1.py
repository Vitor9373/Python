import numpy as np

l = np.zeros(5)
for i in range (5):
    l[i] = int(input(f'Digite o {i+1}º valor: '))
    
maior = l[0]
menor = l[0]
    
for i in range (5):
    if l[i] > maior:
        maior = l[i]
    elif l[i] < menor:
        menor = l[i]
        
print(f'{l} \n possui {maior} como maior número, e {menor} como menor número.')
