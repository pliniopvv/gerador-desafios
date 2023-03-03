import random

# Define a função que gera uma questão aleatória sobre o sistema de amortização PRICE
def generate_question():
    # Define o valor do empréstimo
    loan_amount = random.uniform(1000, 1000000)
    
    # Define a taxa de juros
    interest_rate = random.uniform(0.05, 0.5)
    
    # Define o número de períodos
    n_periods = random.randint(1, 30)
    
    # Calcula a prestação mensal pelo sistema PRICE
    monthly_payment = (loan_amount * interest_rate) / (1 - (1 + interest_rate)**(-n_periods))
    
    # Gera a questão com os valores obtidos
    question = f"Qual o valor da prestação mensal de um empréstimo de R${loan_amount:.2f}, com taxa de juros de {interest_rate:.2%} ao mês, no sistema de amortização PRICE, em {n_periods} meses?"
    
    # Define a resposta correta
    correct_answer = f"O valor da prestação mensal é de R${monthly_payment:.2f}."
    
    return (question, correct_answer)

# Define a função que verifica a resposta do usuário
def check_answer(question, correct_answer, user_answer):
    if user_answer == correct_answer:
        return "Resposta correta!"
    else:
        return "Resposta incorreta. A resposta correta é: " + correct_answer

# Gera uma questão aleatória e solicita que o usuário responda
question, correct_answer = generate_question()
print(question)
user_answer = input("Resposta: ")

# Verifica a resposta do usuário e exibe o resultado
print(check_answer(question, correct_answer, user_answer))
