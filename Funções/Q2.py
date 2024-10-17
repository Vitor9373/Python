x = 0

def par(x):
    if x % 2 == 0:
        return True
    else:
        return False
    
x = int(input('Digite o valor x: '))
print(par(x))