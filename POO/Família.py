class Pessoa:
    nome = ''
    idade = 0
    endereco = ''
    cpf = 0
    sexo = ''
    
    def __init__(self, nome, idade, endereco, cpf, sexo):
        self.nome = nome
        self.idade = idade
        self.endereco = endereco
        self.cpf = cpf
        self.sexo = sexo
    
    def resumo(self, nome, idade, endereco, cpf, sexo):
        print('nome: ', self.nome)
        print('idade: ', self.idade)
        print('endereço: ', self.endereco)
        print('CPF: ', self.cpf)
        print('sexo: ', self.sexo)



class Pai(Pessoa):
    def __init__(self, nome, idade, endereco, cpf, sexo, filhos, esposa):
        super().__init__(nome, idade, endereco, cpf, sexo)
        self.filhos = []
        self.esposa = esposa

    def resumo(self):
        print('Filhos: ', Filho.nome)
        print('Esposa: ', Mae.nome)


class Mae(Pessoa):
    def __init__(self, nome, idade, endereco, cpf, sexo, filhos, esposo):
        super().__init__(nome, idade, endereco, cpf, sexo)
        self.filhos = filhos
        self.esposo = esposo

    def resumo(self):   
        print('Filhos: ', Filho.nome)
        print('Esposo: ', Pai.nome)



class Filho(Pessoa):
    def __init__(self, nome, idade, endereco, cpf, sexo, pai, mae):
        super().__init__(nome, idade, endereco, cpf, sexo)
        self.pai = pai
        self.mae = mae

    def resumo(self):  
        print('Pai: ', Pai.nome)
        print('Mae: ', Mae.nome)

pai = Pai('XX', 20, 'Fundao', 999999, 'Masculino')
mae = Mae('YY', 25, 'Fundao', 999999, 'Feminino')
filho = Filho('FF', 5, 'Fundao', 000000, 'Masculino')
pai.resumo()
mae.resumo()
filho.resumo()