#from Veiculo import Veiculo
from Automovel import Automovel

class Moto(Automovel):
    
	def __init__(self, marca, qtdRodas, modelo, partida):
		super().__init__(marca, qtdRodas, modelo)
		self.partidaEletrica = partida

	def __str__(self) -> str:
		texto = super().__str__() + "\nPartida Elétrica: " 
		if self.partidaEletrica:
			texto += "Sim"
		else:
			texto += "Não"
		return texto
	
	def imprimirInformacoes(self):
		print( self )