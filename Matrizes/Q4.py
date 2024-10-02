m = [[0 for _ in range(5)] for _ in range(5)]
s = 0

for i in range (5):
    for j in range (5):
        m[i][j] = int(input(f'Digite o valor da {i+1}ª linha e {j+1}ª coluna: '))
        if i == 4:
             s += m[i][j]
             
print(f'A soma dos valores da linha quatro é: {s}.')