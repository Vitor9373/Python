m = [[0 for _ in range(5)] for _ in range(5)]

for i in range (5):
    for j in range (5):
        m[i][j] = int(input(f'Digite o valor da {i+1}ª linha e {j+1}ª coluna: '))
        
print('Os valores nas diagonais principais são: ')
            
for i in range (5):
    print(m[i][i])