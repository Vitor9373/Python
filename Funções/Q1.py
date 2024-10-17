x = 0
y = 0

def maior(x,y):
    if x > y:
        return x
    else:
        return y
    
x = int(input('Digite o valor x: '))
y = int(input('Digite o valor y: '))
print('O maior valor é ', maior(x,y))