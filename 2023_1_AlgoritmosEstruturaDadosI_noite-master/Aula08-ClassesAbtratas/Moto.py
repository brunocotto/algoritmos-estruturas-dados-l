from Veiculo import Veiculo

class Moto(Veiculo):

    def __init__(self, modelo=None, ano=None, cilindradas = None):
        super().__init__(modelo, ano)
        self.cilindradas = cilindradas

    def imprimirEspecifico(self):
        super().imprimir()
        print("Cilistradas: ", self.cilindradas)