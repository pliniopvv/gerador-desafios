import random

loan1 = 200000
loan2 = 300000
n1_period = 1
n2_period = 2
n_periods = 2
carencia_periods = 2
taxa = 0.02

question = f"""
Uma empresa tem obrigações perante um credor da seguinte forma:
R${loan1} com vencimento em {n1_period} mês e
R${loan2} com vencimento em {n2_period}.
Considerando que não conseguirá saldar a dívida como anteriormente pactudas,
a mesma empresa propõe uma restruturação, de modo que possa pagar sua dívida em {n_periods}
meses seguidos, a partir de {carencia_periods}, sendo as {n_periods} parcelas do mesmo valor.
Considerando que a taxa de juros utilizada para todas as operações é de {taxa*100:.2f}% ao mês,
o valor de cada uma das parcelas na restruturação será, em reais, de?
"""

def check_answer(question, correct_answer, user_answer):
    if (user_answer - correct_answer) <= 0.01:
        return "Resposta correta!"
    else:
        return "Resposta incorreta. A resposta correta é: " + correct_answer



correct_answer = 



print(question)

