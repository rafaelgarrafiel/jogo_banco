from .propriedade import Propriedade
from random import randrange

class Tabuleiro():
    def __init__(self) -> None:
        self.propriedades = []
        self.jogadores = []
        self.vencedor = None
    
    def inicia_tabuleiro(self):
        for und in range(1, 21):
            self.propriedades.append(Propriedade(randrange(30, 50, 5), randrange(20, 100, 5), None, und))
        return self.propriedades
    
    def verifica_posicao(self, atual, rolagem):
        posicao = atual + rolagem
        volta = 0
        if posicao > 20:
            posicao = posicao - 20
            volta = 1
        return posicao, volta
    
    def jogada(self, jogador):
        rolagem = jogador.rolagem_dado()
        print(f'Jogador tirou: {rolagem}')
        posicao, volta = self.verifica_posicao(jogador.posicao_tabuleiro, rolagem)
        jogador.posicao_tabuleiro = posicao
        if volta:
            print(f'Jogador {jogador.comportamento} completou uma volta')
            jogador.receber(100) 

        if self.propriedades[jogador.posicao_tabuleiro -1].proprietario==None:
            print('Não tem proprietario no imóvel')
            resultado = jogador.deve_comprar(self.propriedades[jogador.posicao_tabuleiro -1])
            if resultado:
                print(f'Jogador: {jogador.comportamento} vai comprar {self.propriedades[jogador.posicao_tabuleiro -1].posicao}')
                continua_jogo = jogador.sacar(self.propriedades[jogador.posicao_tabuleiro -1].custo_venda)
                jogador.jogando = continua_jogo
                if continua_jogo == False:
                    print(f'Jogador {jogador.comportamento} esta negativo')
                    self.remove_jogador(jogador)
                else:
                    self.propriedades[jogador.posicao_tabuleiro -1].proprietario = jogador
        elif self.propriedades[jogador.posicao_tabuleiro -1].proprietario!=jogador:
            print(f'Jogador {jogador.comportamento} vai pagar aluguel para {self.propriedades[jogador.posicao_tabuleiro -1].proprietario.comportamento}')
            continua_jogo = jogador.sacar(self.propriedades[jogador.posicao_tabuleiro -1].valor_aluguel)
            jogador.jogando = continua_jogo
            if continua_jogo == False:
                print(f'Jogador {jogador.comportamento} está negativo')
                self.remove_jogador(jogador)

    def remove_jogador(self, jogador):
        self.jogadores.remove(jogador)
        for propriedade in self.propriedades:
            if propriedade.proprietario == jogador:
                propriedade.proprietario = None
    
    def verifica_vencedor(self, rodada):
        if len(self.jogadores) != 1:
            if rodada == 1000:
                self.vencedor = self.jogadores[0]
                for jogador in self.jogadores:        
                    if jogador.saldo > self.vencedor.saldo:
                        self.vencedor = jogador
                    elif jogador.saldo == self.vencedor.saldo:
                        if jogador.ordem_turno > self.vencedor.ordem_turno:
                            self.vencedor = jogador
                    return True
            else:
                return False
        else:
            self.vencedor = self.jogadores[0]
            return True