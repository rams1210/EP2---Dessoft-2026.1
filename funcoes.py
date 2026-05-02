import random

def rolar_dados(n):
    dados_rolados = []
    i = 0
    while i < n:
        valor = random.randint(1, 6)
        dados_rolados.append(valor)
        i += 1
    return dados_rolados

def guardar_dado(dados_rolados, dados_no_estoque, indice):
    # so guarda um dado por vez, dado_para_guardar = posicao do dado que deseja guardar na lista dados_rolados
    # essa funcao deve transferir o dado escolhido da lista dados_rolados para a lista dados_no_estoque.
    # indice remove o elemento da lista dados_rolados e coloca esse elemento na lista dados_no_estoque

    dado_para_guardar = dados_rolados[indice]
    del dados_rolados[indice]
    dados_no_estoque.append(dado_para_guardar)
    return [dados_rolados, dados_no_estoque]

def remover_dado(dados_rolados, dados_no_estoque, indice2):
    # indice2 remove o elemento da lista dados_no_estoque e coloca esse elemento na lista dados_rolados (dados na mesa)

    dado_para_tirar = dados_no_estoque[indice2]
    del dados_no_estoque[indice2]
    dados_rolados.append(dado_para_tirar)
    return [dados_rolados, dados_no_estoque]
