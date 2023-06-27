from Livro import Livro
from Pilha import Pilha

l1 = Livro("O tempo e o vento", "Érico Veríssimo", 500)
l2 = Livro("Dom Casmurro", "Machado de Assis", 1000)
l3 = Livro("Macunaíma", "Mário de Andrade", 800)
pilha = Pilha()
pilha.add(l1)
pilha.add(l2)
pilha.add(l3)

pilha.remover()
pilha.remover()
pilha.remover()
