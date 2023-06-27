from Fisica import Fisica
from Cidade import Cidade
#from Pessoa import Pessoa
from Fisica import Fisica
from Juridica import Juridica

c1 = Cidade("POA")
c2 = Cidade("Capão da Canoa")

pf1 = Fisica("João", "3322-4455", c1, "000.111.222-33")
pj1 = Juridica("Mercado do Zé", "98765-4321", c2, "00.111.222/0001-02" )
pf2 = Fisica("Maria", "2233-4455", c2, "555.444.333-22")


#pf.imprimir()
pj1.imprimir()

pj1.addFuncionario(pf1)
pj1.addFuncionario(pf2)

pj1.imprimir()