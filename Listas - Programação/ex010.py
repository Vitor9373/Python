# Faça um Programa que leia dois vetores com 10 elementos cada. Gere um terceiro vetor de 20 elementos, 
# cujos valores deverão ser compostos pelos elementos intercalados dos dois outros vetores. 

    v1 = []
    v2 = []
    v3 = []

    print('Digite valores inteiros para o primeiro vetor')
    for i in range (10):
        v1.append(int(input(f'{i+1}º:')))

    print('Digite valores inteiros para o segundo vetor')
    for i in range (10):
        v2.append(int(input(f'{i+1}º:')))
        
    for i in range (10):
        v3.append(v1[i])
        v3.append(v2[i])
        
    print('Terceiro vetor: ',v3)