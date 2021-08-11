from .jogador import Jogador

class JogadorExigente(Jogador):
    def __init__(self, comportamento) -> None:
        super().__init__(comportamento)