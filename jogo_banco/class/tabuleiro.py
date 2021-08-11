from .propriedade import Propriedade
from random import randint

class Tabuleiro():
    def __init__(self) -> None:
        self.propriedades = []
        self.jogadores = []
    
    def inicia_tabuleiro(self):
        for und in range(20):
            self.propriedades.append(Propriedade(randint(30, 50, 5), randint(20, 40, 5), None, und))
        return self.propriedades