from abc import ABC, abstractmethod
class Veiculo(ABC):

    def __init__(self, modelo = None, ano=None):
        self.modelo = modelo
        self.ano = ano

    def imprimir(self):
        print("Modelo: ", self.modelo)
        print("Ano: ", self.ano)

    @abstractmethod
    def imprimirEspecifico(self):
        pass

