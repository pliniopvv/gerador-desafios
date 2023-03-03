import random

# Define a taxa de juros nominal e a taxa de inflação esperada
juros_nominal = 1.2
inflacao_esperada = 0.5

# Gera um valor aleatório para o saldo da aplicação financeira
saldo = random.randint(100000, 1000000)

# Calcula a renda mensal perpétua com base no saldo e nas taxas definidas
renda_mensal = saldo * (juros_nominal - inflacao_esperada) / 100

# Imprime a pergunta para o usuário
print("Um investidor possui um saldo de R$ {:.2f} em uma aplicação financeira, com uma taxa de juros nominal de {}% e uma taxa de inflação esperada de {}% ao mês. Qual seria a renda mensal perpétua, constante em termos reais, que ele poderia obter com esse investimento?".format(saldo, juros_nominal, inflacao_esperada))

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
