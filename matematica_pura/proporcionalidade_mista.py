import random

# Gera uma questão de proporcionalidade mista
def generate_question():
    a = random.randint(1, 10)
    b = random.randint(1, 10)
    c = random.randint(1, 10)
    d = random.randint(1, 10)
    
    if random.randint(0, 1):
        question = f"Se {a} está para {b} assim como {c} está para X, qual é o valor de X se {d} está para {b}?"
        answer = c * d / a
    else:
        question = f"Se {a} está para {b} assim como X está para {c}, qual é o valor de X se {d} está para {b}?"
        answer = c * b / a
    
    return question, answer

# Teste do código
q, a = generate_question()
print(q)
print(a)
