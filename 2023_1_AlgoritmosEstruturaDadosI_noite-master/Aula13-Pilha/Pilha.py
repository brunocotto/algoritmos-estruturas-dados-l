from Livro import Livro
class Pilha:
    def __init__(self):
        self.topo = None
        self.tamanho = 0

    def add(self, livro):
        if self.topo == None:
            self.topo = livro
        else:
            livro.proximo = self.topo
            self.topo = livro
        self.tamanho += 1
        self.imprimir()
    
    def imprimir(self):
        print("-----------")
        if self.topo == None:
            print("Pilha Vazia")
        else:
            aux = self.topo
            while( aux ):
                print( aux )
                aux = aux.proximo 
                print("-----------") 
            print("Total de elementos: ", str(self.tamanho) )
    


    def remover(self):
        if self.topo == None:
            print("Pilha Vazia")
        else:
            self.topo = self.topo.proximo
            self.tamanho -= 1
            self.imprimir()

    










            