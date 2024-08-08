A = []
B = []
C = []

for i in range (5):
    A.append(int(input(f'Digite o {i+1}° valor da lista: ')))

for i in range (5):
     B.append(int(input(f'Digite o {i+1}° valor da segunda lista: ')))
     
C = A + B
print(C)