from Conta import Conta

c1 = Conta()

# print( c1.getSaldo() )

# c1.setSaldo(20)

# print( "Novo saldo: " + str(c1.getSaldo()) )

print("Saldo: " + str( c1.saldo ) )
c1.saldo = 30
print( "Novo saldo: " + str(c1.saldo) )

c1.depositar(100)
print( "Saldo após dep: " + str(c1.saldo) )
c1.sacar(200)
print( "Saldo após Saque: " + str(c1.saldo) )
