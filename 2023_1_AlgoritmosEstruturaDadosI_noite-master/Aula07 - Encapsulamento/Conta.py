class Conta:
	logado = True
	tarifa = 1.99

	def __init__(self):
		self.__saldo = 0.0

	def getSaldo(self):
		if self.logado:
			return self.__saldo
		else:
			return "Acesso negado"
		
	def setSaldo(self, valor):
		if self.logado:
			self.__saldo = valor
		else:
			print("Acesso negado")

	# Método Acessor
	@property
	def saldo(self):
		if self.logado:
	 		return self.__saldo
		else:
			return "Acesso negado"		
	# Método Modificador
	@saldo.setter
	def saldo(self, valor):
		if self.logado:
	 		self.__saldo = valor
		else:
			print("Acesso negado")

	def __descontarTarifa(self):
		self.__saldo -= self.tarifa
		
	def depositar(self, valor):
		if self.__saldo + valor >= self.tarifa:
			self.__saldo += valor
			self.__descontarTarifa()
		else: 
			print("Valor insuficiente")	
	def sacar(self, valor):
		if self.__saldo - valor >= self.tarifa:
			self.__saldo -= valor
			self.__descontarTarifa()
		else: 
			print("Saldo insuficiente")
