from No import No
class Lista:
    def __init__(self):
        self.inicio = None
        self.tamanho = 0
    
    def add(self, valor):
        nodo = No(valor)
        if self.inicio == None:
            self.inicio = nodo
        else:   
            if self.inicio.dado >= nodo.dado:
                nodo.proximo = self.inicio
                self.inicio = nodo
            else: 
                aux = self.inicio.proximo
                ant = self.inicio
                while aux :
                    if nodo.dado < aux.dado :
                        ant.proximo = nodo
                        nodo.proximo = aux
                        break
                    else:
                        ant = aux
                        aux = aux.proximo
                if aux == None and nodo.dado >= ant.dado:
                    ant.proximo = nodo
        self.tamanho += 1
        self.imprimir()

    def imprimir(self):
        if self.inicio == None:
            print( "Lista Vazia" )
        else:
            print("-----------")
            aux = self.inicio
            while( aux ):
                print( aux.dado )
                aux = aux.proximo
            print("Total de elementos: ", str(self.tamanho) )
    

    def remover(self, valor ):
        tamAnterior = self.tamanho
        if self.inicio == None:
            print("Lista Vazia")
            #Lista contendo apenas 1 elemento e este é igual ao valor
        elif self.inicio.proximo == None and self.inicio.dado == valor:
            self.inicio = None
            self.tamanho = 0
            self.imprimir()
        else:
            #Lista contendo vários elementos e o valor está na primeira posição
            if self.inicio.dado == valor:
                self.inicio = self.inicio.proximo
                self.tamanho -= 1
            #Lista contendo vários elementos e o valor está no meio da lista
            else:
                ant = self.inicio
                aux = self.inicio.proximo
                while aux:
                    if aux.dado == valor:
                        ant.proximo = aux.proximo
                        self.tamanho -= 1
                        break
                    else:
                        ant = aux
                        aux = aux.proximo
        if self.tamanho < tamAnterior :
            print( "Valor não encontrado")
        self.imprimir()












            