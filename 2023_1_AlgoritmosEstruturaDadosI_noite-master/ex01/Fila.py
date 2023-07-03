class Fila:
    def __init__(self):
        self.primeiro = None
        self.ultimo = None

    def adicionar_apartamento(self, apartamento):
        if self.primeiro is None:
            self.primeiro = apartamento
        else:
            self.ultimo.proximo = apartamento
        self.ultimo = apartamento

    def retirar_apartamento(self, numero_vaga):
        atual = self.primeiro
        anterior = None
        while atual:
            if atual.numero_vaga_garagem == numero_vaga:
                if anterior:
                    anterior.proximo = atual.proximo
                    if atual == self.ultimo:
                        self.ultimo = anterior
                else:
                    self.primeiro = atual.proximo
                    if atual == self.ultimo:
                        self.ultimo = None
                return atual
            anterior = atual
            atual = atual.proximo
        return None

    def imprimir(self):
        atual = self.primeiro
        while atual:
            atual.imprimir()
            print("=-"*20)
            atual = atual.proximo