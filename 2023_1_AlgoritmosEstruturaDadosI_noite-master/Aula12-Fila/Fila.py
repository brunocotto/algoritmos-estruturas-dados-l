from No import No
class Fila:
    def __init__(self):
        self.primeiro = None
        self.ultimo = None
        self.tamanho = 0

    def add(self, valor):
        nodo = No(valor)
        if self.primeiro == None:
            self.primeiro = nodo
            self.ultimo = nodo
        else:
            self.ultimo.proximo = nodo
            self.ultimo = nodo
        self.tamanho += 1
        self.imprimir()
    
    def imprimir(self):
        texto = ""
        if self.primeiro == None:
            texto = "Lista Vazia"
        else:
            aux = self.primeiro
            while( aux ):
                texto += str(aux.dado) + " - " 
                aux = aux.proximo
        print("-----------")
        print( texto )
        print("Total de elementos: ", str(self.tamanho) )
    


    def remover(self):
        if self.primeiro == None:
            print("Lista Vazia")
        elif self.primeiro.proximo == None:
            self.primeiro = None
            self.ultimo = None
            self.tamanho = 0
        else:
            self.primeiro = self.primeiro.proximo
            self.tamanho -= 1
        self.imprimir()

    










            