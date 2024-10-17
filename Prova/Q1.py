import numpy as np

a = np.zeros(8)
x = np.zeros(8)
y = np.zeros(8)

for i in range (0,8):
    a[i] = int(input(f'Digite o {i+1}º número: '))
    if a[i] > 0:
        x[i] = a[i]
    elif a[i] < 0:
        y[i] = a[i]
        
print('Variável original: ')
for i in range (0,8):
    if a[i] != 0:
        print(a[i])


print('Variável positiva: ')
for i in range (0,8):
    if x[i] != 0:
        print(x[i])

print('Variável negativa: ')
for i in range (0,8):
    if y[i] != 0:
        print(y[i])