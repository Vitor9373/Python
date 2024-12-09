#Foram anotadas as idades e alturas de 30 alunos. 
#Faça um Programa que determine quantos alunos com mais de 13 anos possuem altura inferior à média de altura desses alunos. 

idades = []
alturas = []
somaAlturas = 0
media = 0
quant = 0

for i in range (30):
    idades.append(int(input(f'Digite a idade do aluno {i+1}: ')))
    alturas.append(float(input(f'Digite a altura do aluno {i+1}: ')))
    somaAlturas = somaAlturas + alturas[i]
    
media = somaAlturas / 30

for i in range (30):
    if idades[i] > 13 and alturas[i] < media:
        quant += 1
        
print(f'Existem {quant} alunos com mais de 13 anos e altura inferior a média.')