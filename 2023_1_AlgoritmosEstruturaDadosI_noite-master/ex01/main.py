from Torre import Torre
from Fila import Fila
from Apartamento import Apartamento

# Criando uma torre
torre1 = Torre(1, "Torre A", "Rua Principal")
torre1.cadastrar()

# Criando apartamentos
apartamento1 = Apartamento(1, 101, 1, torre1)
apartamento2 = Apartamento(2, 102, 2, torre1)
apartamento3 = Apartamento(3, 103, 3, torre1)

# Criando a fila de espera
fila_espera = Fila()
fila_espera.adicionar_apartamento(apartamento2)
fila_espera.adicionar_apartamento(apartamento3)

# Imprimindo informações da torre
print("Informações da Torre:")
torre1.imprimir()
print("=-"*20)

# Imprimindo informações dos apartamentos
print("Informações do Apartamento 1:")
apartamento1.imprimir()
print("=-"*20)

print("Informações do Apartamento 2:")
apartamento2.imprimir()
print("=-"*20)

print("Informações do Apartamento 3:")
apartamento3.imprimir()
print("=-"*20)

# Imprimindo fila de espera
print("Fila de Espera:")
fila_espera.imprimir()

# Retirando apartamento da fila de espera
numero_vaga = 2
apartamento_retirado = fila_espera.retirar_apartamento(numero_vaga)
if apartamento_retirado:
    print(f"O apartamento com número de vaga {numero_vaga} foi retirado da fila de espera.")
else:
    print(f"Nenhum apartamento com número de vaga {numero_vaga} foi encontrado na fila de espera.")

# Imprimindo fila de espera atualizada
print("Fila de Espera Atualizada:")
fila_espera.imprimir()


