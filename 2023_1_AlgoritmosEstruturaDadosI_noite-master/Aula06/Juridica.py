from Pessoa import Pessoa
#from Fisica import Fisica
#from Cidade import Cidade

class Juridica( Pessoa ):

    def __init__(self, nome, fone, cidade, cnpj = None ):
        super().__init__(nome, fone, cidade)
        self.cnpj = cnpj
        self.funcionarios = []


    def addFuncionario( self,  pFisica ):
        self.funcionarios.append( pFisica )

    def imprimir(self):
        super().imprimir()
        print("CNPJ: " , self.cnpj)
        print("Funcionários: \n--------------------")
        if len(self.funcionarios) == 0:
            print("Não possui funcionários")
        else:
            for pFisica in self.funcionarios:
                print("Nome Func.:" , pFisica.nome)
                print("Fone: ", pFisica.fone)
                print("Cidade: ", pFisica.city.nome)
                print("--------------------")

        def __str__(self):
            texto = "Empresa: " + self.nome
            texto += "\nFone: " + self.fone
            texto += "\nCNPJ: " + self.cnpj
            return texto