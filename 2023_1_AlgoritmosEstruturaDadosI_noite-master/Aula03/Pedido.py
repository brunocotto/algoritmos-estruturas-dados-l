class Pedido:
    def __init__(self, data, endereco, cliente):
        self.id = None
        self.data = data
        self.end = endereco
        self.cliente = cliente
        self.produtos = []

    def imprimir(self):
        print("Data: ", self.data)
        print("Endereço: ", self.end)
        print("Cliente: ", self.cliente.nome)
        print("Cidade: ", self.cliente.city.nome)
        print("Produtos: ")
        total = 0
        if len( self.produtos ) == 0:
            print("Pedido Vazio!")
        else:
            for prod in self.produtos:
                total += prod.preco
                print("-------------")
                print("Produto: ", prod.nome)
                print("Preço: ", prod.preco)
                print("Categoria: ", prod.categoria.nome)
            print("-------------")
            print("Total: ", total)
                
    def addProduto(self, produto):
        self.produtos.append( produto )
        total = 0
        for prod in self.produtos:
            total += prod.preco
        return total