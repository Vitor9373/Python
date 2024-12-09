#Faça um programa que calcule as raízes de uma equação do segundo grau, na forma ax2 + bx + c. 
# O programa deverá pedir os valores de a, b e c e fazer as consistências, informando ao usuário nas seguintes situações:
#Se o usuário informar o valor de A igual a zero, 
# a equação não é do segundo grau e o programa não deve fazer pedir os demais valores, sendo encerrado;
#Se o delta calculado for negativo, a equação não possui raízes reais. Informe ao usuário e encerre o programa;
#Se o delta calculado for igual a zero a equação possui apenas uma raiz real; informe-a ao usuário;
#Se o delta for positivo, a equação possui duas raiz reais; informe-as ao usuário;

while True:
    a = int(input('Digite o valor de a: '))
    if a == 0:
        print('A equação não é de segundo grau, pois "a" é 0.')
        break
    b = int(input('Digite o valor de b: '))
    c = int(input('Digite o valor de c: '))
    delta = (b*b) - (4 * a * c)
    if delta < 0:
        print('A equação não possuí raízes reais.')
        break
    elif delta == 0:
        x1 = (-b + delta ** 0.5) / (2 * a)
        print(f'A raiz da equação é {x1}.')
    else:
        x1 = (-b + delta ** 0.5) / (2 * a)
        x2 = (-b - delta ** 0.5) / (2 * a)
        print(f'A Raiz 1 é {x1}, e a 2 {x2}.')