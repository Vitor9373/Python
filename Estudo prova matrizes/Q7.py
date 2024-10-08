import numpy as np

x = np.zeros(10)

for i in range (0,10):
    x[i] = int(input(f'Digite o {i+1}º valor: '))

print(x,'\n')

a = set(x)
a = {int(num) for num in a}

print(a)