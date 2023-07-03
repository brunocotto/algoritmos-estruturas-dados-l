class Torre:
    def __init__(self, id, nome, endereco):
        self.id = id
        self.nome = nome
        self.endereco = endereco

    def cadastrar(self):
        # Poderia adicionar a torre em uma lista
        pass

    def imprimir(self):
        print(f"ID: {self.id}")
        print(f"Nome: {self.nome}")
        print(f"Endereço: {self.endereco}")
