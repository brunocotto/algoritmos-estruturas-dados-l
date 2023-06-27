def busca_sequencial(vetor, elemento):
    contador = 0
    # laço no vetor
    for i in range(len(vetor)):
        contador += 1
        # se o vetor[i] == ao elemento, retorna o contador e i(valor procurado)
        if vetor[i] == elemento:
            # retorna o número de iterações e o índice do elemento encontrado
            return contador, i  
    # retorna o número de iterações e -1 se o elemento não for encontrado
    return contador, -1  

def busca_binaria(vetor, elemento):
    contador = 0
    inicio = 0
    fim = len(vetor) - 1
    # enquanto o início não for menor ou igual o fim, executa
    while inicio <= fim:
        contador += 1
        # variável que calcula o meio após cada laço
        meio = (inicio + fim) // 2
        # verifica se o meio do vetor é igual ao elemento, retorna se sim
        if vetor[meio] == elemento:
            # retorna o número de iterações e o índice do elemento encontrado
            return contador, meio 
        # ou se, verifica se o meio é MENOR que o elemento 
        elif vetor[meio] < elemento:
            # se o meio é menor que o elemento o inicio = meio + 1
            inicio = meio + 1
        # se não, meio é MAIOR que o elemento, ou seja, fim = meio - 1
        else:
            fim = meio - 1
    # retorna o número de iterações e -1 se o elemento não for encontrado
    return contador, -1  

# simulação do vetor
vetor = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160, 170, 180, 190, 200]

# peço para o usuário entrar com o elemento que deseja procurar
elemento = int(input("Informe o valor que deseja procurar: "))
print("=-"*25)

# função de busca sequencial 
seq_iteracoes, seq_indice = busca_sequencial(vetor, elemento)

# se o indíce retornado for diferente de -1
if seq_indice != -1:
    print(f'O elemento {elemento} foi encontrado no índice {seq_indice}.')
else:
    print(f'O elemento {elemento} não foi encontrado no vetor.')
print(f'O número de iterações na busca sequencial foi: {seq_iteracoes}')
print("=-"*25)



# A busca binária exige que o vetor esteja ordenado
vetor.sort() 
# função de busca binária
bin_iteracoes, bin_indice = busca_binaria(vetor, elemento)

if bin_indice != -1:
    print(f'O elemento {elemento} foi encontrado no índice {bin_indice}.')
else:
    print(f'O elemento {elemento} não foi encontrado no vetor.')
print(f'O número de iterações na busca binária foi: {bin_iteracoes}')
print("=-"*25)

