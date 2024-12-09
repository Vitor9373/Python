#O Hipermercado Tabajara está com uma promoção de carnes que é imperdível. Confira:
#                            Até 5 Kg                  Acima de 5 Kg
#Filé Duplo       R$ 4,90 por Kg          R$ 5,80 por Kg
#Alcatra          R$ 5,90 por Kg          R$ 6,80 por Kg
#Picanha          R$ 6,90 por Kg          R$ 7,80 por Kg
#Para atender a todos os clientes, cada cliente poderá levar apenas um dos tipos de carne da promoção,
#porém não há limites para a quantidade de carne por cliente. 
#Se compra for feita no cartão Tabajara o cliente receberá ainda um desconto de 5% sobre o total da compra. 
#Escreva um programa que peça o tipo e a quantidade de carne comprada pelo usuário e gere um cupom fiscal, 
#contendo as informações da compra: tipo e quantidade de carne, preço total, tipo de pagamento, valor do desconto e valor a pagar.

tipo = int(input('Digite o tipo de carne que deseja comprar:\n1-Filé duplo\n2-Alcatra\n3-Picanha\n:'))
quant = float(input('Digite quantos Kg deseja comprar: '))
pag = input('Qual pagamento irá usar? (P-pix, C-cartão, D-dinheiro, L-cartão da loja):').upper()
preco = 0
precoTotal = 0
valorDesconto = 0

if tipo == 1:
    tipo == 'Filé duplo'
    if quant <= 5:
        precoTotal = quant * 4.9
    else:
        precoTotal = quant * 5.8
    if pag == 'L':
        preco = precoTotal * 0.95
elif tipo == 2:
    tipo == 'Alcatra'
    if quant <= 5:
        precoTotal = quant * 5.9
    else:
        precoTotal = quant * 6.8
    if pag == 'L':
        preco = precoTotal * 0.95
elif tipo == 3:
    tipo == 'Picanha'
    if quant <= 5:
        precoTotal = quant * 6.9
    else:
        precoTotal = quant * 7.8
    if pag == 'L':
        preco = precoTotal * 0.95
valorDesconto = precoTotal - precoTotal * 0.95

print('------------------------------------------------------------------------------')
print(f'Tipo de carne: {tipo};\nQuantidade de carne: {quant};\nPreço total: {precoTotal:.2f};\nTipo de pagamento: {pag};\nValor do desconto:{valorDesconto:.2f};\nValor a pagar: {preco}.')