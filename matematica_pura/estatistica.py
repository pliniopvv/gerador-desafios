import random

def questao_media_amostral(numeros):
    """
    Gera uma questão sobre cálculo de média amostral.
    :param numeros: lista de números para calcular a média amostral.
    :return: string com a questão e a resposta correta.
    """
    media = sum(numeros) / len(numeros)
    questao = f"Qual a média amostral dos seguintes números: {numeros}?"
    resposta = f"A média amostral é: {media:.2f}"
    return questao, resposta

def questao_mediana(numeros):
    """
    Gera uma questão sobre cálculo de mediana.
    :param numeros: lista de números para calcular a mediana.
    :return: string com a questão e a resposta correta.
    """
    numeros_ordenados = sorted(numeros)
    if len(numeros_ordenados) % 2 == 0:
        mediana = (numeros_ordenados[len(numeros_ordenados)//2 - 1] + numeros_ordenados[len(numeros_ordenados)//2]) / 2
    else:
        mediana = numeros_ordenados[len(numeros_ordenados)//2]
    questao = f"Qual a mediana dos seguintes números: {numeros}?"
    resposta = f"A mediana é: {mediana}"
    return questao, resposta

def questao_desvio_padrao(numeros):
    """
    Gera uma questão sobre cálculo de desvio padrão.
    :param numeros: lista de números para calcular o desvio padrão.
    :return: string com a questão e a resposta correta.
    """
    media = sum(numeros) / len(numeros)
    variancia = sum([(x - media)**2 for x in numeros]) / len(numeros)
    desvio_padrao = variancia**0.5
    questao = f"Qual o desvio padrão dos seguintes números: {numeros}?"
    resposta = f"O desvio padrão é: {desvio_padrao:.2f}"
    return questao, resposta

# Exemplo de uso do código para gerar uma questão aleatória
numeros = [random.randint(1, 10) for _ in range(10)]
tipo_questao = random.choice([questao_media_amostral, questao_mediana, questao_desvio_padrao])
questao, resposta = tipo_questao(numeros)
print(questao)
print(resposta)
