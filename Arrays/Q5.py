import numpy as np

n = 10
v = np.zeros(n)

for i in range(10):
    v[i] = int(input(f'Digite o {i+1}° numero: '))
maior = v[0]
menor = v[0]
menorP = 0
maiorP = 0
    
for j in range(10):
    if v[j] < menor:
          menorP = j
    elif v[j] > maior:
        maiorP = j

print(f'O maior valor do vetor esta na posicao {maiorP+1}, e o menor valor esta na posicao {menorP+1}')  