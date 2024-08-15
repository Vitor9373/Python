f = input('Digite uma frase: ')
t = len(f)
for i in range(t):
    if f[i] != '.':
        print(f[i], f.count(f[i]), 'x')
        f = f.replace(f[i], '.')