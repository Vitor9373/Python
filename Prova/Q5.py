import numpy as np

x = np.zeros(3)
m = np.zeros((3, 3))
r = np.zeros((3, 3))

for i in range (0,3):
    x[i] = int(input(f'Digite o {i+1}º valor do vetor: '))
    
for i in range (0,3):
    for j in range (0,3):
        m[i][j] = int(input(f'Digite o valor da posicao ({i},{j}): '))
        
for i in range (0,3):
    for j in range (0,3):
        r[i][j] = m[j][i] * x[i]
        
print(r)