import pandas as pd
from random import choice
from classes.tabuleiro import Tabuleiro
from classes.jogador import Jogador


def main():
    vencedor = [] 
    turnos = [] 
    limites = 0

    for und in range(1, 300):

        # Iniciando o tabuleiro
        tabuleiro = Tabuleiro()
        tabuleiro.inicia_tabuleiro()


        # Preparando os jogadores
        comportamentos = ["Impulsivo", "Exigente", "Cauteloso", "Aleatorio"]
        for ordem in range(1, 5):
            escolha = choice(comportamentos)
            comportamentos.remove(escolha)
            tabuleiro.jogadores.append(Jogador(escolha, ordem))
        # for und in tabuleiro.jogadores:
        #     print(f'O jogador {und} possui a posição {und.ordem_turno}')

        inicio = True
        rodada = 1
        while inicio:

            for jogador in tabuleiro.jogadores:
                if jogador.jogando:
                    tabuleiro.jogada(jogador)


            verifica, limite = tabuleiro.verifica_vencedor(rodada)
            if verifica:
                vencedor.append(tabuleiro.vencedor.comportamento)
                turnos.append(rodada)
                if limite:
                    limites += 1
                inicio = False
            else:
                rodada += 1
        
        print(f'O vencedor eh: {tabuleiro.vencedor}, seu saldo eh: {tabuleiro.vencedor.saldo}')

    df = pd.DataFrame({"vencedores": vencedor, "turnos": turnos})
    jogadores = ((df['vencedores'].value_counts() / df['vencedores'].count()) * 100)

    print("==========================================")

    print(f'O total de partidas terminadas por time out eh: {limites}')

    media = df['turnos'].mean()
    print(f'A media de turnos de uma partida eh: {round(media,2)}')

    print('O percentual de vitorias para cada comportamento eh:')
    for und in jogadores.iteritems():
        print(f'{und[0]} => {round(und[1],2)}')
    # print(jogadores)

    vencedor = df['vencedores'].describe()['top']
    print(f'O maior vencedor eh {vencedor}')
    

if __name__ == "__main__":
    main()