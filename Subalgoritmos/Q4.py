x = 0
y = 0
ope = 0

def calculadora(x,y,ope):
    r = 0
    match(ope):
        case 1:
            r = x + y
        case 2:
            r = x - y
        case 3:
            r = x * y
        case 4:
            x / y
    return r

x = int(input('Digite o primeiro valor: '))
y = int(input('Digite o segundo valor: '))
ope = int(input('Digite a operação de que deseja realizar:\n 1- soma\n 2- subtração\n 3- multiplicação\n 4- divisão\n :'))
if ope == 1 or ope == 2 or ope == 3 or ope == 4:
    print('O resultado da operação é ', calculadora(x,y,ope))
else:
    print('Operação inválida')