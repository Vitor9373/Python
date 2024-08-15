f = input('Digite sua frase: ')
f = f.upper()
p = f[::-1].upper()
if f == p:
    print('Essa frase é um palíndromo.')
else:
    print('Essa frase não é um palíndromo')