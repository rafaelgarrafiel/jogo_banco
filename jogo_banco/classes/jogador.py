from random import randint

class Jogador():
    def __init__(self, comportamento, ordem_turno) -> None:
        self.saldo = 300
        self.comportamento = comportamento
        self.ordem_turno = ordem_turno
        self.posicao_tabuleiro = 0
        self.jogando = True
    
    def __str__(self):
        return self.comportamento
    
    def rolagem_dado(self):
        return randint(1, 6)

    def sacar(self, valor):
        self.saldo -= valor 
        return self.saldo
    
    def receber(self, valor):
        self.saldo += valor
        return self.saldo
    
    def deve_comprar(self, propriedade):
        if self.comportamento == "Impulsivo":
            print('Jogador é impulsivo e vai comprar o imóvel')
            return True
        elif self.comportamento == "Exigente":
            if propriedade.custo_venda > 50:
                return True
            else:
                print(f'Jogador é exigente, a propriedade custa {propriedade.custo_venda}')
        elif self.comportamento == "Cauteloso":
            if self.saldo - propriedade.custo_venda > 80:
                return True
            else:
                print(f'Jogador é Cauteloso, a propriedade custa {propriedade.custo_venda} e seu saldo é {self.saldo}')
        elif self.comportamento == "Aleatorio":
            if randint(1, 2) == 1:
                return True
            else:
                print('Jogador aleatório não estava com vontade')
    def verifica_saldo(self):
        return self.saldo

