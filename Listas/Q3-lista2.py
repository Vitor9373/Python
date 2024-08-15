d = input('Digite sua data de nascimento: ')
d = d.split('/')

if d[1] == '01':
    m = 'janeiro'
elif d[1] == '02':
    m = 'fevereiro'
elif d[1] == '03':
    m = 'março'
elif d[1] == '04':
    m = 'abril'
elif d[1] == '05':
    m = 'maio'
elif d[1] == '06':
    m = 'junho'
elif d[1] == '07':
    m = 'julho'
elif d[1] == '08':
    m = 'agosto'
elif d[1] == '09':
    m = 'setembro'
elif d[1] == '10':
    m = 'outubro'
elif d[1] == '11':
    m = 'novembro'
elif d[1] == '12':
    m = 'dezembro'

print(f'Você nasceu em {d[0]} de {m} de {d[2]}.')