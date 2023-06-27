from Veiculo import Veiculo

class Automovel(Veiculo):
    
	def __init__(self, marca, qtdRodas, modelo, potencia):
		super().__init__(marca, qtdRodas, modelo)
		self.potenciaDoMotor = potencia

	def __str__(self) -> str:
		texto = super().__str__() + "\nPotência do Motor: " + self.potenciaDoMotor 
		return texto
	
	def imprimirInformacoes(self):
		print( self )


        

        