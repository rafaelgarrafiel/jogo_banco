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
        # for ordem in range(1, 5):
        #     tabuleiro.jogadores.append(Jogador(choice(["Impulsivo", "Exigente", "Cauteloso", "Aleatorio"]), ordem))
        tabuleiro.jogadores.append(Jogador("Impulsivo", 1))
        tabuleiro.jogadores.append(Jogador("Exigente", 2))
        tabuleiro.jogadores.append(Jogador("Cauteloso", 3))
        tabuleiro.jogadores.append(Jogador("Aleatorio", 4))

        inicio = True
        rodada = 1
        while inicio:

            for jogador in tabuleiro.jogadores:
                print(f'Jogador atual é: {jogador.comportamento}, sua posição é {jogador.posicao_tabuleiro}')
                if jogador.jogando:
                    tabuleiro.jogada(jogador)


            verifica = tabuleiro.verifica_vencedor(rodada)
            if verifica:
                inicio = False
            else:
                print('Mapa da rodada')
                for und in tabuleiro.propriedades:
                    print(f'A propriedade {und.posicao} => {und.proprietario}')
                print(f'Rodada {rodada}, sem vencedor!')
                rodada += 1
        
        print(f'O vencedor é: {tabuleiro.vencedor}, seu saldo é: {tabuleiro.vencedor.saldo}')

if __name__ == "__main__":
    main()