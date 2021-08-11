from .jogador import Jogador

class JogadorImpulsivo(Jogador):
    def __init__(self, comportamento) -> None:
        super().__init__(comportamento)