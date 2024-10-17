import numpy as np

m = np.zeros((6, 6))
aux = 1

for i in range (0,6):
    for j in range(0,6):
        m[i][j] = aux
        aux += 1

for j in range (0,6):
    m[1][j] = m[4][j]
    
for i in range (0,6):
    m[i][3] = m[i][4]

print(m)