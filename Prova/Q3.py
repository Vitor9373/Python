import numpy as np

x = np.zeros(100)
pares = 0
impares = 0
SomaImpares = 0
mediaImpares = 0

for i in range (0,100):
    x[i] = i+1
    if x[i] % 2 == 0:
        pares += 1
    else:
        impares += 1
        SomaImpares += x[i]

mediaImpares = SomaImpares / impares
print(f'Foram armazenados {pares} valores pares na lista.')
print(f'A média dos valores ímpares é {mediaImpares}.')