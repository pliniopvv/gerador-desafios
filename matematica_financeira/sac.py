import random

# função que gera uma questão sobre SAC
def gerar_questao_sac():
    # gerar valores aleatórios para o saldo devedor, taxa de juros e número de períodos
    saldo_devedor = random.uniform(10000, 100000)
    taxa_juros = random.uniform(0.01, 0.05)
    num_periodos = random.randint(10, 30)
    
    # calcular o valor da prestação e o total de juros pagos
    prestacao = saldo_devedor * ((taxa_juros * (1 + taxa_juros) ** num_periodos) / ((1 + taxa_juros) ** num_periodos - 1))
    juros_pagos = prestacao * num_periodos - saldo_devedor
    
    # criar a questão como uma string formatada
    questao = f"Um empréstimo de R${saldo_devedor:.2f} foi feito com uma taxa de juros de {taxa_juros:.2%} ao período. O empréstimo foi pago em {num_periodos} parcelas iguais. Qual o valor da prestação e o total de juros pagos?\n"
    questao += f"A) Prestação: R${prestacao:.2f}, juros totais pagos: R${juros_pagos:.2f}\n"
    questao += f"B) Prestação: R${prestacao * 1.1:.2f}, juros totais pagos: R${juros_pagos * 1.1:.2f}\n"
    questao += f"C) Prestação: R${prestacao * 0.9:.2f}, juros totais pagos: R${juros_pagos * 0.9:.2f}\n"
    questao += f"D) Prestação: R${prestacao * 1.2:.2f}, juros totais pagos: R${juros_pagos * 1.2:.2f}\n"
    
    return questao

# função principal que gera um número de questões especificado pelo usuário
def main():
    num_questoes = int(input("Quantas questões deseja gerar? "))
    
    for i in range(num_questoes):
        print(gerar_questao_sac())
        print("-" * 50)

if __name__ == '__main__':
    main()
