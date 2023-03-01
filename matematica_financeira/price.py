import random

# Define a função que gera uma questão aleatória sobre o sistema de amortização PRICE
def generate_question():
    # Define o valor do empréstimo
    loan_amount = random.uniform(1000, 1000000)
    
    # Define a taxa de juros
    interest_rate = random.uniform(0.05, 0.5)
    
    # Define o número de períodos
    n_periods = random.randint(1, 30)
    
    # Define um mês meta para cálculo dos juros
    monthly_meta = random.randint(1, n_periods)
    
    # dados do desafio extraído.
    # loan_amount = 15000
    # n_periods = 18
    # interest_rate = 0.02
    # monthly_meta = 10

    # Calcula a prestação mensal pelo sistema PRICE
    monthly_payment = (loan_amount * interest_rate) / (1 - (1 + interest_rate)**(-n_periods))
    
    # Prevendo resultado
    first_juros = loan_amount * (1 + interest_rate) - loan_amount # Juros do primeiro mês
    first_amortization = monthly_payment - first_juros # Amortização do primeiro mês descontado o primeiro mês
    meta_amortization = first_amortization * (1 + interest_rate) ** (monthly_meta-1)
    meta_juros = monthly_payment - meta_amortization

    # Gera a questão com os valores obtidos
    question = f"Um empréstimo contraído no mês X0, no valor de R${loan_amount:.2f} deve ser pago em {n_periods} prestações mensais iguais, a uma taxa de juros compostos de {interest_rate*100:.2f}% ao mês, vencendo a primeira prestação no fim do mês X0, a segunda no fim de X1 e assim sucessivamente. Calcule quanto está sendo pago de juros na {monthly_meta} prestação."
    
    # Define a resposta correta
    correct_answer = f"O valor da prestação mensal é de R${monthly_payment:.2f}. E o valor dos juros na {monthly_meta} parcela é de R${meta_juros:.2f}."
    
    return (question, correct_answer)

# Define a função que verifica a resposta do usuário
def check_answer(question, correct_answer, user_answer):
    if (int(user_answer) - correct_answer) <= 0.01:
        return "Resposta correta!"
    else:
        return "Resposta incorreta. A resposta correta é: " + correct_answer

# Gera uma questão aleatória e solicita que o usuário responda
question, correct_answer = generate_question()
print(question)
user_answer = input("Resposta: ")

# Verifica a resposta do usuário e exibe o resultado
print(check_answer(question, correct_answer, user_answer))
