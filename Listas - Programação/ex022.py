#Sua organização acaba de contratar um estagiário para trabalhar no Suporte de Informática, 
# com a intenção de fazer um levantamento nas sucatas encontradas nesta área. 
# A primeira tarefa dele é testar todos os cerca de 200 mouses que se encontram lá,
# testando e anotando o estado de cada um deles, para verificar o que se pode aproveitar deles. 
#Foi requisitado que você desenvolva um programa para registrar este levantamento. 
# O programa deverá receber um número indeterminado de entradas, cada uma contendo: 
# um número de identificação do mouse o tipo de defeito: necessita da esfera; 
#necessita de limpeza; a.necessita troca do cabo ou conector;
# a.quebrado ou inutilizado Uma identificação igual a zero encerra o programa.


defeitos = {
        1: {"descricao": "Necessita da esfera", "quantidade": 0},
        2: {"descricao": "Necessita de limpeza", "quantidade": 0},
        3: {"descricao": "Necessita troca do cabo ou conector", "quantidade": 0},
        4: {"descricao": "Quebrado ou inutilizado", "quantidade": 0},
    }

total_mouses = 0

print("Registro de Mouses Defeituosos\n")
print("Tipos de defeitos:")
print("1 - Necessita da esfera")
print("2 - Necessita de limpeza")
print("3 - Necessita troca do cabo ou conector")
print("4 - Quebrado ou inutilizado")
print("Digite 0 para encerrar o programa.\n")

while True: 
    tipo_defeito = int(input("Tipo de defeito: "))
    if tipo_defeito == 0:
        break
    elif tipo_defeito in defeitos:
        defeitos[tipo_defeito]["quantidade"] += 1
        total_mouses += 1
    else:
        print("Tipo de defeito inválido. Tente novamente.")

print("\nRelatório Final\n")
print(f"Total de mouses analisados: {total_mouses}\n")
print("Defeitos registrados:")
for tipo, info in defeitos.items():
    percentual = (info["quantidade"] / total_mouses * 100) if total_mouses > 0 else 0
    print(f"{tipo} - {info['descricao']}: {info['quantidade']} ({percentual:.2f}%)")