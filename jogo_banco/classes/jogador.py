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
        if self.saldo < 0:
            return False
        else:
            return True
    
    def receber(self, valor):
        self.saldo += valor
        return self.saldo
    
    def deve_comprar(self, propriedade):
        if self.comportamento == "Impulsivo":
            print('Jogador eh impulsivo e vai comprar o imovel')
            return True
        elif self.comportamento == "Exigente":
            if propriedade.valor_aluguel > 50:
                return True
            else:
                print(f'Jogador eh exigente, a propriedade custa {propriedade.custo_venda}')
        elif self.comportamento == "Cauteloso":
            if self.saldo - propriedade.custo_venda > 80:
                return True
            else:
                print(f'Jogador eh Cauteloso, a propriedade custa {propriedade.custo_venda} e seu saldo eh {self.saldo}')
        elif self.comportamento == "Aleatorio":
            if randint(1, 2) == 1:
                return True
            else:
                print('Jogador aleatorio nao estava com vontade')


