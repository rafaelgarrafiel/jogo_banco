from .propriedade import Propriedade
from random import randrange

class Tabuleiro():
    def __init__(self) -> None:
        self.propriedades = []
        self.jogadores = []
        self.vencedor = None
    
    def inicia_tabuleiro(self):
        for und in range(1, 21):
            self.propriedades.append(Propriedade(randrange(30, 50, 5), randrange(20, 40, 5), None, und))
        return self.propriedades
    
    def verifica_posicao(self, atual, rolagem):
        posicao = atual + rolagem
        volta = 0
        if posicao > 20:
            posicao = posicao - 20
            volta = 1
        return posicao, volta
    
    def roda_jogada(self, jogador):
        rolagem = jogador.rolagem_dado()
        posicao, volta = self.verifica_posicao(jogador.posicao_tabuleiro, rolagem)
        jogador.posicao_tabuleiro = posicao
        if volta:
            jogador.receber(100) 

        if self.propriedades[jogador.posicao_tabuleiro].proprietario==None:
            resultado = jogador.deve_comprar(self.propriedades[jogador.posicao_tabuleiro])
            if resultado:
                jogador.sacar(self.propriedades[jogador.posicao_tabuleiro].custo_venda)

        
    
    def verifica_vencedor(self, rodada):
        if rodada == 5:
            self.vencedor = self.jogadores[0]
            return True
        else:
            return False