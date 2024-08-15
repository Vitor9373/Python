f = input('Digite sua frase: ')
f2 = input('Digite outra frase: ')
f = f.upper()
f2 = f2.upper()
if f.find(f2) >= 0 :
  print(f'{f2} encontrado na posição {f.find(f2)}')
else:
    print('Não foi encontrado.')

