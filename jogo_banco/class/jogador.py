from random import randint

class Jogador():
    def __init__(self, comportamento) -> None:
        self.saldo = 300
        self.comportamento = comportamento
        self.ordem_turno = 0
        self.posicao_tabuleiro = 0
    
    def __str__(self):
        return self.comportamento
    
    def rolagem_dado(self):
        return randint(1, 6)
        
    def sacar(self, valor):
        self.saldo -= valor 
        return self.saldo
    
    def receber(self, valor):
        self.saldo += 100
        return self.saldo
    
    def verifica_saldo(self):
        return self.saldo

