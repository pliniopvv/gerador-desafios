import random

def sac(pv, j, n):
    """Calcula as parcelas e o total pago no SAC"""
    amortizacao = pv/n
    saldo_devedor = pv
    prestacoes = []
    total_pago = 0
    for i in range(n):
        juros = saldo_devedor * j
        prestacao = amortizacao + juros
        saldo_devedor -= amortizacao
        total_pago += prestacao
        prestacoes.append(prestacao)
    return (prestacoes, total_pago)

def gerar_questao():
    """Gera uma questão sobre SAC"""
    pv = random.randint(1000, 10000)
    j = random.uniform(0.01, 0.05)
    n = random.randint(10, 30)
    prestacoes, total_pago = sac(pv, j, n)
    resposta = f"R$ {total_pago:.2f}"
    enunciado = f"Considerando um empréstimo de R$ {pv:.2f} a uma taxa de juros compostos de {j:.2%} ao mês, com {n} parcelas iguais, calcule o total pago pelo Sistema de Amortização Contínua (SAC)."
    return (enunciado, resposta)

# Exemplo de uso
enunciado, resposta = gerar_questao()
print(enunciado)
print(resposta)
