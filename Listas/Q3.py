x = []
y = []
soma = 0

for i in range (5):
    x.append(int(input(f'Digite o {i+1}° valor: ')))
    soma += x[i]
    
for i in range (5):
    y.append(int(input(f'Digite o {i+1}° valor da 2ª lista: ')))
    soma += y[i]

print(f'A soma dos valores das listas é {soma}')