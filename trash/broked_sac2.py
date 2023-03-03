import random

def sac(capital, taxa, periodos):
    amortizacao = capital * (taxa / (1 - (1 + taxa)**-periodos))
    saldo_devedor = capital
    for periodo in range(periodos):
        juros = saldo_devedor * taxa
        saldo_devedor = saldo_devedor - (amortizacao - juros)
        yield (amortizacao, juros, saldo_devedor)

def gerar_questoes(num_questoes):
    questoes = []
    for i in range(num_questoes):
        capital = random.uniform(1000, 10000)
        taxa = random.uniform(0.01, 0.05)
        periodos = random.randint(10, 30)
        questao = f"Qual o valor da amortização no período {periodos} para um empréstimo de R${capital:.2f}, com taxa de {taxa*100:.2f}% a.a. pelo SAC?"
        resposta = f"R${next(sac(capital, taxa, periodos))[0]:.2f}"
        questoes.append((questao, resposta))
    return questoes

# Exemplo de uso
questoes = gerar_questoes(5)
for questao, resposta in questoes:
    print(questao)
    r = input("Resposta: ")
    print(f"Correta: {resposta}, Sua resposta: {r}")
