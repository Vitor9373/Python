# Faça um Programa que peça as quatro notas de 10 alunos, 
# calcule e armazene num vetor a média de cada aluno, 
# imprima o número de alunos com média maior ou igual a 7.0.

medias = []
aprovados = 0

for i in range (10):
    n1 = float(input(f'Digite as notas do {i+1}º aluno\n1ª:'))
    n2 = float(input('2ª: '))
    n3 = float(input('3ª: '))
    n4 = float(input('4ª: '))
    media = (n1 + n2 + n3 + n4) / 4
    medias.append(media)
    if media >= 7:
        aprovados += 1

print(f'Tiveram {aprovados} aluno(s) com média maior ou igual a 7.')