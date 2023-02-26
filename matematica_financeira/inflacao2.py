import random

# Define a taxa de juros nominal e a taxa de inflação esperada
juros_nominal = random.uniform(0.05,5.0)
inflacao_esperada = random.uniform(0.1,10.0)

# Gera um valor aleatório para o saldo da aplicação financeira
saldo = random.randint(100, 5000)

# Calcula a renda mensal perpétua com base no saldo e nas taxas definidas
renda_mensal = saldo * ((1 + (juros_nominal/100) * (1 + (inflacao_esperada/100))) - 1)
# Imprime a pergunta para o usuário
print("No ano de X1, o dono de um imóvel recebia um aluguel de R$ {:.2f}. No ano de X2, será firmado um contrato de aluguel com um novo inquilino. O proprietário deseja um aumento real de {:.2f}%. Sabendo que a inflação do período foi de {:.2f}%, qual o valor do aumento REAL do aluguel?".format(saldo, juros_nominal, inflacao_esperada))

# Imprime as opções de resposta para o usuário
print("a) R$ {:.2f}".format(renda_mensal * 0.5))
print("b) R$ {:.2f}".format(renda_mensal * 0.75))
print("c) R$ {:.2f}".format(renda_mensal))
print("d) R$ {:.2f}".format(renda_mensal * 1.25))
print("e) R$ {:.2f}".format(renda_mensal * 1.5))

# Solicita a resposta do usuário e verifica se está correta
resposta = input("Qual é a opção correta? ")
if resposta == "c":
    print("Parabéns, você acertou!")
else:
    print("Resposta incorreta.")
