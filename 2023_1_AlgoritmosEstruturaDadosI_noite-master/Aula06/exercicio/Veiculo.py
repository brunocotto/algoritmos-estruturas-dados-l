class Veiculo:
    
	def __init__(self, marca, qtdRodas, modelo):
		self.velocidade = 0
		self.marca = marca
		self.qtdRodas = qtdRodas
		self.modelo = modelo

	def acelerar(self, valor):
		self.velocidade += valor

	def frear(self, valor):
		if self.velocidade - valor < 0:
			self.velocidade = 0
		else:
			self.velocidade -= valor
	def __str__(self) -> str:
		texto = "Marca: " + self.marca + "\nQtdRodas: " + self.qtdRodas
		texto += "\nModelo: " + self.modelo + "\nVelocidade Atual: " + self.velocidade
		return texto
	
	def imprimirInformacoes(self):
		print( self )

	



        
