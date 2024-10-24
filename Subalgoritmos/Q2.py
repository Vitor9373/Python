import numpy as np

a = np.zeros((5, 5))
aux = 0

def soma(a):
    s = 0
    for i in range(0,5):
        for j in range(0,5):
            s += a[i][j]
    return s

for i in range(0,5):
    for j in range(0,5):
        a[i][j] = aux
        aux += 1
        
print(a)
print('A soma dos valores da matriz é: ', soma(a))