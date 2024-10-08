import numpy as np

m = np.zeros((3, 3))
s = 0

for i in range (0,3):
    for j in range (0,3):
        m[i][j] = int(input(f'Digite o valor da posição ({i}, {j}):'))
        s += m[i][j]
    
print(f'Matriz completa: \n{m}')
print(f'\n A soma dos valores da matriz é {s}')