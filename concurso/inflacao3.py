import random

# Define a taxa de juros nominal e a taxa de inflação esperada
juros_nominal = random.uniform(5,20.0)
inflacao_X0 = random.uniform(80,90)
inflacao_X1 = random.uniform(inflacao_X0,100)

# juros_nominal = 18
# inflacao_X0 = 80
# inflacao_X1 = 83.2

var_infla = ((inflacao_X1-inflacao_X0) / inflacao_X0)
juros_aparente = ((1 + var_infla) * (1 + (juros_nominal/(4*100))) - 1)*100

# Imprime a pergunta para o usuário
print("""Um investidor fez uma aplicação em um título com rentabilidade pós-fixada por um prazo de três meses a uma taxa de juros simples de {:.2f}% ao ano.
    O índice de correção a ser aplicado ao montante passou de {:.2f}, no início, a {:.2f}, no fim do prazo. Qual o valor mais próximo da rentabilidade total do título nesse prazo?
""".format(juros_nominal, inflacao_X0, inflacao_X1))

# Imprime as opções de resposta para o usuário
print("a) {:.2f}%".format(juros_aparente * 0.5))
print("b) {:.2f}%".format(juros_aparente * 0.75))
print("c) {:.2f}%".format(juros_aparente))
print("d) {:.2f}%".format(juros_aparente * 1.25))
print("e) {:.2f}%".format(juros_aparente * 1.5))

# Solicita a resposta do usuário e verifica se está correta
resposta = input("Qual é a opção correta? ")
if resposta == "c":
    print("Parabéns, você acertou!")
else:
    print("Resposta incorreta.")
