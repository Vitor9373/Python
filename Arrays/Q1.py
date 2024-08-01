import numpy as np

n = 10
v = np.zeros(n)

for i in range(10):
    v[i] = int(input(f'Digite o {i+1}° numero: '))
print(v)