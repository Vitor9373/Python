#Uma grande emissora de televisão quer fazer uma enquete entre os seus telespectadores para saber
# qual o melhor jogador após cada jogo. Para isto, faz-se necessário o desenvolvimento de um programa, 
# que será utilizado pelas telefonistas, para a computação dos votos. 
# Sua equipe foi contratada para desenvolver este programa, 
# utilizando a linguagem de programação C++. Para computar cada voto, 
# a telefonista digitará um número, entre 1 e 23, correspondente ao número da camisa do jogador.
# Um número de jogador igual zero, indica que a votação foi encerrada. 
# Se um número inválido for digitado, o programa deve ignorá-lo, mostrando uma breve mensagem de aviso, 
# e voltando a pedir outro número. Após o final da votação, o programa deverá exibir: 
#a. O total de votos computados; 
#b. Os númeos e respectivos votos de todos os jogadores que receberam votos; 
#c. O percentual de votos de cada um destes jogadores; 
#d. O número do jogador escolhido como o melhor jogador da partida, juntamente com o número de votos e o percentual de votos dados a ele. 

votos = [0] * 24 
total = 0

print("Digite o numero da camisa do jogador (1 a 23) ou 0 para encerrar: ")
while True:
    voto = int(input())
    if voto == 0:
        break
    if voto < 1 or voto > 23:
        print("Numero de jogador invalido. Tente novamente.")
    else:
        votos[voto] += 1
        total += 1

print("\nResultado da votação:")
print(f"Total de votos computados: {total}")

melhor = 0
maior_voto = 0
for i in range(1, 24):
    if votos[i] > 0:
        percentual = (votos[i] * 100.0) / total
        print(f"Jogador {i} recebeu {votos[i]} votos. {percentual:.2f}% dos votos.")
        if votos[i] > maior_voto:
            maior_voto = votos[i]
            melhor = i

if melhor != 0:
    percentual_melhor = (maior_voto * 100.0) / total
    print(f"\nO melhor jogador foi o jogador {melhor} com {maior_voto} votos, que representa {percentual_melhor:.2f}% dos votos.")
else:
        print("Nenhum voto foi computado.")


