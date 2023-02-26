import random

# Função que gera uma questão sobre o sistema de amortização americano
def generate_question():
    # Gerando valores aleatórios para o financiamento
    saldo_devedor = random.randint(100000, 500000)
    taxa_juros = round(random.uniform(0.01, 0.05), 2)
    num_prestacoes = random.randint(12, 60)
    
    # Calculando o valor da prestação e o valor dos juros para o primeiro mês
    juros_mensais = saldo_devedor * taxa_juros
    prestacao = saldo_devedor / num_prestacoes + juros_mensais
    amortizacao = prestacao - juros_mensais
    
    # Gerando a questão
    question = f"Um empréstimo de R${saldo_devedor:.2f} foi concedido a uma taxa de juros mensal de {taxa_juros*100:.2f}%, a ser pago em {num_prestacoes} prestações mensais pelo sistema de amortização americano. Qual é o valor da prestação mensal e dos juros pagos no primeiro mês?"
    answer = f"Valor da prestação: R${prestacao:.2f} / Juros do primeiro mês: R${juros_mensais:.2f}"
    
    return (question, answer)
    
# Testando a função com uma questão aleatória
print(generate_question())
