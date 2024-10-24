import numpy as np

m = np.zeros((4, 4))
aux = 1

def diagonal(m):
    s = 0
    for i in range(0,4):
        for j in range(0,4):
            if i == j:
                s += m[i][j]
    return s

for i in range(0,4):
    for j in range(0,4):
        m[i][j] = aux
        aux += 1
        
print('A soma dos valores da diagonal principal é ', diagonal(m))