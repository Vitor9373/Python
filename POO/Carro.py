class Carro:
    cor = 'Laranja'
    marca = 'Nissan'
    modelo = 'Nismo'
    nome = 'GTR-R35'
    ano = 2020
    km_rodados = 0
    
    status_motor = 'Desligado'
    status_movimento = 'Parado'
    
    def ligarMotor (self, status_motor):
        print('Ligando motor...')
        self.status_motor = 'Ligado'
        
    def DesligarMotor (self, status_motor):
       print('Desligando motor...')
       self.status_motor = 'Desligado'
       
    def andar(self, status_movimento):
        print('Andando')
        self.status_movimento = 'Andando' 
        
    def parar(self, status_movimento):
       print('Parando')
       self.status_movimento = 'Parado'
       
    def status(self, status_movimento, status_motor):
        print('Status motor: ', status_motor)
        print('Status Movimento: ', status_movimento)    