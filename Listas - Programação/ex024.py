#Faça um programa que simule um lançamento de dados. 
# Lance o dado 100 vezes e armazene os resultados em um vetor . 
# Depois, mostre quantas vezes cada valor foi conseguido. 
# Dica: use um vetor de contadores(1-6) e uma função para gerar numeros aleatórios, simulando os lançamentos dos dados.

import random

def rolagem(times):
    contador = [0] * 6
    for _ in range(times):
        result = random.randint(1, 6) 
        contador[result - 1] += 1

    return contador

num_lancamentos = 100 
resultados = rolagem(num_lancamentos)

print("Simulação de lançamentos de dado\n")
print(f"O dado foi lançado {num_lancamentos} vezes.")
print("Resultados:")
for i, contador in enumerate(resultados, start=1):
    print(f"Valor {i}: {contador} vezes")