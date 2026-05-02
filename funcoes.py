import random
def rolar_dados(n):
    dados_rolados = []
    i = 0
    while i < n:
        valor = random.randint(1, 6)
        dados_rolados.append(valor)
        i += 1
    return dados_rolados