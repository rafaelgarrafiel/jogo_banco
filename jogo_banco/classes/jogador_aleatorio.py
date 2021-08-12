from .jogador import Jogador

class JogadorAleatorio(Jogador):
    def __init__(self, comportamento) -> None:
        super().__init__(comportamento)