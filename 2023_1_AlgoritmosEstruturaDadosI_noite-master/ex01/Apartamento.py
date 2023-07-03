class Apartamento:
    def __init__(self, id, numero_apartamento, numero_vaga_garagem, torre, proximo=None):
        self.id = id
        self.numero_apartamento = numero_apartamento
        self.numero_vaga_garagem = numero_vaga_garagem
        self.torre = torre
        self.proximo = proximo

    def cadastrar(self):
        # Lógica para cadastrar o apartamento (pode ser implementada posteriormente)
        pass

    def imprimir(self):
        print(f"ID: {self.id}")
        print(f"Número do Apartamento: {self.numero_apartamento}")
        print(f"Número da Vaga de Garagem: {self.numero_vaga_garagem}")
        print("Torre:")
        self.torre.imprimir()
        if self.proximo:
            print("Próximo Apartamento:")
            self.proximo.imprimir()