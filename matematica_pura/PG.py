import random

def generate_pg_question():
    a1 = random.randint(1, 10)
    r = random.randint(2, 5)
    n = random.randint(3, 6)
    an = a1 * r**(n-1)
    question = f"Qual é o {n}º termo da PG de primeiro termo {a1} e razão {r}?"
    answer = str(an)
    return question, answer
    
q, a = generate_pg_question()
print(q)
user_answer = input("Resposta: ")
if user_answer == a:
    print("Resposta correta!")
else:
    print(f"Resposta incorreta. R: {a}")
