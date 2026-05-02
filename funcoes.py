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

def calcula_pontos_regra_simples(dados_rolados):
    # A cada rodada, sempre que o jogador rola os dados, jogo deverá apresentar a pontuação da combinação atual para as categorias de 1 a 6.
    dicionario = {}
    # dados_rolados = [2, 3, 4, 5, 2]
    dicionario[1] = 0
    dicionario[2] = 0
    dicionario[3] = 0
    dicionario[4] = 0
    dicionario[5] = 0
    dicionario[6] = 0
    for jogada in dados_rolados:
        dicionario[jogada] += jogada
    return dicionario

def calcula_pontos_soma(dados_rolados):
    soma = 0
    for dado in dados_rolados:
        soma += dado
    return soma
