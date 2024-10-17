import numpy as np

x = np.zeros(25)
a = np.zeros(25)
aux = 24

for i in range (0,5):
    x[i] = int(input(f'Digite o {i+1}º valor: '))
    
print('Lista original:')
print(x)

for i in range (0,25):
    a[i] = x[aux]
    aux -= 1
    a[i] = a[i] * -1
    
print('Lista invertida e negativa:')
print(a)
    