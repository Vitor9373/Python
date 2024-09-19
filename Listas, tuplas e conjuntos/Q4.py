x = [1,2,3,4,5,6,7,8,9]
posPrimo = False

print('Os números primos da lista são: ')
    
for i in range(0,9):
    if x[i] > 1:
        posPrimo = True
    for j in range(2, int(x[i] ** 0.5) + 1):
         if x[i] % j == 0:
             posPrimo = False
             break
    if posPrimo:
        print(f'{x[i]} na posição {i}')