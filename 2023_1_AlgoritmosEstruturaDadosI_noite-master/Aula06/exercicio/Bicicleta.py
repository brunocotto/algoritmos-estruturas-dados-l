from Veiculo import Veiculo

class Bicicleta(Veiculo):
    
	def __init__(self, marca, qtdRodas, modelo, marchas, bagageiro):
		super().__init__(marca, qtdRodas, modelo)
		self.numMarchas = marchas
		self.bagageiro = bagageiro

	def __str__(self) -> str:
		texto = super().__str__() + "\nMarchas: " + self.numMarchas 
		texto += "\nBagageiro: "
		if self.bagageiro :
			texto += "Sim"
		else:
			texto += "Não"
		return texto
	
	def imprimirInformacoes(self):
		print( self )


        

        