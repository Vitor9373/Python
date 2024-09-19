k = []

for i in range(20):
    valor = int(input(f'Digite o {i + 1}º valor: '))
    k.append(valor) 

for i in range(0, 19, 2): 
    k[i], k[i + 1] = k[i + 1], k[i] 

print("Lista após as trocas:", k)