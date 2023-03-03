import random

def price(capital, taxa, periodo):
    """
    Calcula o valor da parcela do sistema de amortização PRICE
    """
    valor_parcela = capital * (taxa / (1 - (1 + taxa) ** (-periodo)))
    juros = valor_parcela - capital * taxa
    return valor_parcela, juros

# Valores de exemplo
capital = 10000
taxa = 0.01
periodo = 12

# Calcula o valor da parcela e dos juros
valor_parcela, _ = price(capital, taxa, periodo)

# Gera um mês aleatório para questionar os juros
mes = random.randint(1, periodo)
_, juros_mes = price(capital, taxa, mes)

# Exibe a questão
print(f"Qual o valor dos juros do {mes}º mês de um empréstimo de R$ {capital:.2f} a uma taxa de {taxa*100:.2f}% ao mês pelo sistema de amortização PRICE?")
resposta = float(input("Resposta: "))

# Verifica a resposta
if round(resposta, 2) == round(juros_mes, 2):
    print("Resposta correta!")
else:
    print(f"Resposta incorreta. O valor correto é R$ {juros_mes:.2f}.")
