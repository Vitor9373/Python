#Faça um programa para o cálculo de uma folha de pagamento, 
#sabendo que os descontos são do Imposto de Renda, 
#que depende do salário bruto (conforme tabela abaixo) e 3% para o Sindicato e que o FGTS corresponde a 11% do Salário Bruto, 
#mas não é descontado (é a empresa que deposita). O Salário Líquido corresponde ao Salário Bruto menos os descontos. 
#O programa deverá pedir ao usuário o valor da sua hora e a quantidade de horas trabalhadas no mês.
#Desconto do IR:
#Salário Bruto até 900 (inclusive) - isento
#Salário Bruto até 1500 (inclusive) - desconto de 5%
#Salário Bruto até 2500 (inclusive) - desconto de 10%
vHora = float(input('Digite o valor da sua hora: '))
qHora = int(input('digite quantas horas trabalhou no mês: '))
salBruto = vHora * qHora
sal = salBruto - ((salBruto * 0.97) + (salBruto * 0.89))
if salBruto > 900 and salBruto <= 1500:
    sal = salBruto - salBruto * 0.95
elif salBruto > 1500 and salBruto <= 2500:
    sal = salBruto - salBruto * 0.9
elif salBruto > 2500:
    sal = salBruto - salBruto * 0.8

print(f'\nValor da hora: {vHora}')
print(f'Horas trabalhadas: {qHora}')
print(f'Salário bruto: {salBruto}')
print(f'Salário líquido: {salBruto - sal}')
print('Quantidade de descontos: ', sal)