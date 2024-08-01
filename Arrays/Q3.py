import numpy as np

n = 5
v = np.zeros(n)
s = 0

for i in range(5):
    v[i] = int(input(f'Digite o {i+1}° valor:'))
    s += v[i]
media = s/5
print(f'A media dos valores digitado e {media}')
    