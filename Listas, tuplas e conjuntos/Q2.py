r = {}
a = {}
x = {}

for i in range (1,6):
    r[i] = input('Digite os números da loto: ')
    
for i in range (1,11):
    a[i] = input('Digite os números da aposta: ')
    
x = set (r & a)
p = len(x)

print(f'Você conseguiu {p} pontos.')