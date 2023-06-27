from Veiculo import Veiculo

class Carro(Veiculo):

    def __init__(self, modelo=None, ano=None, qtdPortas = None):
        super().__init__(modelo, ano)
        self.qtdPortas = qtdPortas

    def imprimirEspecifico(self):
        super().imprimir()
        print("\nPoertas: ", self.qtdPortas)