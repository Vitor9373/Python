#As Organizações Tabajara resolveram dar um abono aos seus colaboradores 
# em reconhecimento ao bom resultado alcançado durante o ano que passou. 
# Para isto contratou você para desenvolver a aplicação que servirá 
# como uma projeção de quanto será gasto com o pagamento deste abono. 
#Após reuniões envolvendo a diretoria executiva,
# a diretoria financeira e os representantes do sindicato laboral, chegou-se a seguinte forma de cálculo: 
#a.Cada funcionário receberá o equivalente a 20% do seu salário bruto de dezembro; 
#a.O piso do abono será de 100 reais, isto é, aqueles funcionários cujo salário for muito baixo,
# recebem este valor mínimo; Neste momento, não se deve ter nenhuma preocupação com colaboradores
# com tempo menor de casa, descontos, impostos ou outras particularidades. 
# Seu programa deverá permitir a digitação do salário de um número indefinido (desconhecido) de salários. 
# Um valor de salário igual a 0 (zero) encerra a digitação.
# Após a entrada de todos os dados o programa deverá calcular o valor do abono concedido a cada colaborador, 
# de acordo com a regra definida acima. Ao final, o programa deverá apresentar: 
#O salário de cada funcionário, juntamente com o valor do abono; 
#O número total de funcionário processados; 
#O valor total a ser gasto com o pagamento do abono; 
#O número de funcionário que receberá o valor mínimo de 100 reais; 
#O maior valor pago como abono;

total_abono = 0
total_funcionarios = 0
total_minimo = 0
maior_abono = 0

while True:
    salario = float(input("Digite o salário do funcionário (0 para encerrar): "))

    if salario == 0:
        break
        
    abono = salario * 0.20  
    if abono < 100:
        abono = 100  

    print(f"Salário: R${salario:.2f} | Abono: R${abono:.2f}")

    total_funcionarios += 1
    total_abono += abono

    if abono == 100:
        total_minimo += 1
        
    if abono > maior_abono:
        maior_abono = abono

print("\nResumo dos pagamentos:")
print(f"Total de funcionários processados: {total_funcionarios}")
print(f"Valor total gasto com o pagamento de abonos: R${total_abono:.2f}")
print(f"Número de funcionários que receberam o valor mínimo de 100 reais: {total_minimo}")
print(f"Maior valor de abono pago: R${maior_abono:.2f}")