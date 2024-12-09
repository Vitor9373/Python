    # Altere o programa anterior, intercalando 3 vetores de 10 elementos cada. 

    v1 = []
    v2 = []
    v3 = []
    v4 = []

    print('Digite valores inteiros para o primeiro vetor')
    for i in range (10):
        v1.append(int(input(f'{i+1}º:')))

    print('Digite valores inteiros para o segundo vetor')
    for i in range (10):
        v2.append(int(input(f'{i+1}º:')))
        
    print('Digite valores inteiros para o terceiro vetor')
    for i in range (10):
        v3.append(int(input(f'{i+1}º:')))
        
    for i in range (10):
        v4.append(v1[i])
        v4.append(v2[i])
        v4.append(v3[i])
        
    print('Vetor final: ',v4)