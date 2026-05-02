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

def calcula_pontos_sequencia_baixa(dados_rolados):
    # 3 combinacoes possiveis de sequencias baixas: [1,2,3,4] / [2,3,4,5] / [3,4,5,6]
    # dados rolados: ordenar e tirar repetidos

    n = len(dados_rolados)
    for i in range(n):
        for j in range(0, n - i - 1):
            if dados_rolados[j] > dados_rolados[j + 1]:
                dados_rolados[j], dados_rolados[j + 1] = dados_rolados[j + 1], dados_rolados[j]
    valores_unicos = []
    for dado in dados_rolados:
        if dado not in valores_unicos:
            valores_unicos.append(dado)
    if len(valores_unicos) < 4:
        return 0
    contador_sequencia = 1
    for i in range(len(valores_unicos) - 1):
        if valores_unicos[i+1] == valores_unicos[i] + 1:
            contador_sequencia += 1
            if contador_sequencia == 4:
                return 15
        else:
            contador_sequencia = 1
    return 0

def calcula_pontos_sequencia_alta(dados_rolados):
    n = len(dados_rolados)
    for i in range(n):
        for j in range(0, n - i - 1):
            if dados_rolados[j] > dados_rolados[j + 1]:
                dados_rolados[j], dados_rolados[j + 1] = dados_rolados[j + 1], dados_rolados[j]
    valores_unicos = []
    for dado in dados_rolados:
        if dado not in valores_unicos:
            valores_unicos.append(dado)
    if len(valores_unicos) < 5:
        return 0
    contador_sequencia = 1
    for i in range(len(valores_unicos) - 1):
        if valores_unicos[i+1] == valores_unicos[i] + 1:
            contador_sequencia += 1
            if contador_sequencia == 5:
                return 30
        else:
            contador_sequencia = 1
    return 0

def calcula_pontos_full_house(dados_rolados):
    # a lista dados_rolados deve ter uma trinca e um par, com valores da trinca e par diferentes entre si, n pode ter 3/+ valores diferentes, n pode ter apenas 1 valor diferente
    n = len(dados_rolados)
    for i in range(n):
        for j in range(0, n - i - 1):
            if dados_rolados[j] > dados_rolados[j + 1]:
                dados_rolados[j], dados_rolados[j + 1] = dados_rolados[j + 1], dados_rolados[j]
    contagens = []
    valores_unicos = []
    for dado in dados_rolados:
        if dado not in valores_unicos:
            valores_unicos.append(dado)
    if len(valores_unicos) != 2:
        return 0
    frequencias = []
    for valor in valores_unicos:
        qtd = 0
        for dado in dados_rolados:
            if dado == valor:
                qtd += 1
        frequencias.append(qtd)
    tem_trinca = False
    tem_par = False
    for f in frequencias:
        if f == 3:
            tem_trinca = True
        if f == 2:
            tem_par = True
    if tem_trinca and tem_par:
        soma_total = 0
        for dado in dados_rolados:
            soma_total += dado
        return soma_total
    return 0

def calcula_pontos_quadra(dados_rolados):
    # deve haver um valor que aparece 4x
    valores_unicos = []
    for dado in dados_rolados:
        if dado not in valores_unicos:
            valores_unicos.append(dado)
    tem_quadra = False
    for valor in valores_unicos:
        qtd = 0
        for dado in dados_rolados:
            if dado == valor:
                qtd += 1
        if qtd >= 4:
            tem_quadra = True
    if tem_quadra:
        soma_total = 0
        for d in dados_rolados:
            soma_total += d
        return soma_total
    return 0

def calcula_pontos_quina(dados_rolados):
    # pelo menos 5 valores =
    valores_unicos = []
    for dado in dados_rolados:
        if dado not in valores_unicos:
            valores_unicos.append(dado)
    tem_quina = False
    for valor in valores_unicos:
        qtd = 0
        for dado in dados_rolados:
            if dado == valor:
                qtd += 1
        if qtd >= 5:
            tem_quina = True
    if tem_quina:
        return 50
    return 0

def calcula_pontos_regra_avancada(dados_rolados):
    pontuacoes = {
        'sem_combinacao': calcula_pontos_soma(dados_rolados),
        'sequencia_baixa': calcula_pontos_sequencia_baixa(dados_rolados),
        'sequencia_alta': calcula_pontos_sequencia_alta(dados_rolados),
        'full_house': calcula_pontos_full_house(dados_rolados),
        'quadra': calcula_pontos_quadra(dados_rolados),
        'cinco_iguais': calcula_pontos_quina(dados_rolados)
    }

    return pontuacoes