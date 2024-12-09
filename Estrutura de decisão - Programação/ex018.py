#Faça um Programa que peça uma data no formato dd/mm/aaaa e determine se a mesma é uma data válida.

d = int(input('Digite uma data no formato dd/mm/aaaa:\nDia:'))
m = int(input('Mês: '))
a = int(input('Ano: '))

if a > 0:
    if m > 0 and m < 12:
        if m == 1 or m == 3 or m == 5 or m == 7 or m == 8 or m == 10 or m == 12:
            if d > 0 and d <= 31:
                print('A data está correta.')
            else:
                print('A data está incorreta.')
        elif m == 4 or m == 6 or m == 9 or m == 11:
            if d > 0 and d <= 30:
                print('A data está correta.')
            else:
                print('A data está incorreta.')
        else:
            if a % 4 == 0:
                if d > 0 and d <= 29:
                    print('A data está correta.')
                else:
                    print('A data está incorreta.')
            else:
                if d > 0 and d <= 28:
                    print('A data está correta.')
                else:
                    print('A data está incorreta.')