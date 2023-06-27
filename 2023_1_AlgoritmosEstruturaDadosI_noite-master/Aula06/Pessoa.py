from Cidade import Cidade

class Pessoa:
        def __init__(self, name=None, fone=None, cidade=None):
            self.id = None
            self.nome = name
            self.fone = fone
            self.city = cidade

        def imprimir(self):
            print("Nome: ", self.nome)
            print("Telefone: ", self.fone)
            print("Cidade: ", self.city.nome )

        def __str__(self):
            texto = "Nome: " + self.nome
            texto += "\nFone: " + self.fone
            return texto