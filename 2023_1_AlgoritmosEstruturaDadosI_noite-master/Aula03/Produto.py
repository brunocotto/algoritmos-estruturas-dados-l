class Produto:
    def __init__(self, name, preco, cat):
        self.id = None
        self.nome = name
        self.preco = preco
        self.categoria = cat
    
    def imprimir(self):
        print("Nome: ", self.nome)
        print("Preço: ", self.preco)
        print("Categoria: ", self.categoria.nome )

    
