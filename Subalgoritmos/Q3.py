import numpy as np

v = np.zeros(15)

def trocar(v):
    a = np.zeros(15)
    for i in range(0,15):
        if v[i] > 0:
            a[i] = v[i]
        else:
            a[i] = 0
    return a

for i in range(0,15):
    v[i] = int(input(f'Digite o valor {i+1} para o vetor: '))
    
print(v, '\n')
print(trocar(v))