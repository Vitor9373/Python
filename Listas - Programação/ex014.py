# Utilizando listas faça um programa que faça 5 perguntas para uma pessoa sobre um crime. As perguntas são: 
#a. "Telefonou para a vítima?" 
#b. "Esteve no local do crime?" 
#c. "Mora perto da vítima?" 
#d. "Devia para a vítima?" 
#e. "Já trabalhou com a vítima?" O programa deve no final emitir uma classificação sobre a participação da pessoa no crime. 
# Se a pessoa responder positivamente a 2 questões ela deve ser classificada como "Suspeita",
# entre 3 e 4 como "Cúmplice" e 5 como "Assassino". Caso contrário, ele será classificado como "Inocente".

perguntas = ['Telefonou para a vítima?','Esteve no local do crime?', 'Mora perto da vítima?','Devia para a vítima?','Já trabalhou com a vítima?']
part = 0
cla = ''

print('Responda (0 para não, e 1 para sim) as perguntas seguintes:')
for i in range (5):
    while True:
        resposta = int(input(f'{perguntas[i]}\nR:'))
        if resposta == 1:
            part += 1
            break
        elif resposta == 0:
            pass
            break
        else:
            print('Resposta incorreta! Digite novamente.')

if part == 2:
    cla = 'suspeito'
elif part == 3 or part == 4:
    cla = 'cúmplice'
elif part == 5:
    cla = 'assassino'
else:
    cla = 'inocente'
    
print(f'Você foi classificado como {cla} no caso.')