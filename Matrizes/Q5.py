m = [[0 for _ in range(10)] for _ in range(10)]
aux = 1
som2 = 0
somp = 0

for i in range (10):
    for j in range (10):
        m[i][j] = aux
        aux += 1
        if j == 2:
            som2 += m[i][j]
        if i == j:
            somp += m[i][j]

print(f'A coluna 2 tem somatório {som2}\n e a diagonal principal tem somatório {somp}')