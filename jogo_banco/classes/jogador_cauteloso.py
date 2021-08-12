from .jogador import Jogador

class JogadorCauteloso(Jogador):
    def __init__(self, comportamento) -> None:
        super().__init__(comportamento)