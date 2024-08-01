import numpy as np

n = 5
v = np.zeros(n)
s = 0

for i in range(5):
    v[i] = int(input(f'Digite o {i+1}° numero: '))
    s += v[i]
print(f'o somatorio dos valores e {s}')