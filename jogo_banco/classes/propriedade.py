
class Propriedade():

    def __init__(self, custo_venda = 0, valor_aluguel = 0, proprietario = None, posicao = 0) -> None:
        self.custo_venda = custo_venda
        self.valor_aluguel = valor_aluguel
        self.proprietario = proprietario
        self.posicao = posicao
    
    def situacao_propriedade(self):
        return bool(self.proprietario)
    
    def vender_propriedade(self, jogador):
        self.proprietario = jogador