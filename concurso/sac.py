import random

valor_total = random.uniform(10000, 999999)
total_parcelas = random.randint(5,48)
taxa_juros = random.uniform(0.005, 0.09)
meta_mes = random.randint(5,total_parcelas)

# valor_total = 487554.90
# total_parcelas = 32
# taxa_juros = 0.0792
# meta_mes = 25

def solver():
    valor_parcela = valor_total / total_parcelas
    SD = valor_total - valor_parcela*(meta_mes-1)
    juros = SD*taxa_juros
    return juros

preambulo = f"Foi realizado um empréstimo no valor de R$ {valor_total:.2f}, com total de {total_parcelas} parcelas, e taxa de juros de {taxa_juros*100:.2f}%, pelo sistema SAC."
questao = f"Qual o valor dos juros pagos na prestação do mês {meta_mes}?"

print(preambulo)
print(questao)
saldo_juros = solver()
resposta = float(input("Sua Resposta: "))
if (saldo_juros - resposta) <= 0.01:
    print(f"Resposta certa! R:{saldo_juros:.2f}")
else:
    print(f"Resposta errada: {saldo_juros:.2f}")