from classes.tabuleiro import Tabuleiro
from classes.jogador import Jogador
from random import choice


def main():
    partidas = []

    for und in range(1, 11):

        # Iniciando o tabuleiro
        tabuleiro = Tabuleiro()
        tabuleiro.inicia_tabuleiro()

        # Preparando os jogadores
        for ordem in range(1, 5):
            tabuleiro.jogadores.append(Jogador(choice(["Impulsivo", "Exigente", "Cauteloso", "Aleatorio"]), ordem))

        inicio = True
        rodada = 1
        while inicio:

            for jogador in tabuleiro.jogadores:
                rolagem = jogador.rolagem_dado()

                jogador.posicao_atual += rolagem 

            verifica = tabuleiro.verifica_vencedor(rodada)
            if verifica:
                inicio = False
            else:
                print(f'Rodada {rodada}, sem vencedor!')
                rodada += 1
        
        print(f'O vencedor é: {tabuleiro.vencedor}')

if __name__ == "__main__":
    main()