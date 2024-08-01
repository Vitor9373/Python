import numpy as np

n = 5
v = np.zeros(n)
maior = 0
menor = 0

for i in range(5):
    v[i] = int(input(f'Digite o {i+1}° valor: '))
menor = v[0]
maior = v[0]
    
for j in range(5):
    if v[j] < menor:
        menor = v[j]
    elif v[j] > maior:
        maior = v[j]

print(f'O maior valor digitado e {maior}, e o menor e {menor}')