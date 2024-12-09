#Faça um Programa que leia um vetor de 10 caracteres, e diga quantas consoantes foram lidas. Imprima as consoantes

v = []
c = []
s = 0

for i in range (10):
    v.append(input('Digite 10 letras: ').upper())
    if v[i] != 'A' and v[i] != 'E' and v[i] != 'I' and v[i] != 'O' and v[i] != 'U':
        s += 1
        c.append(v[i])

print(f'Foram lidas {s} consoantes, sendo essas: {c}')