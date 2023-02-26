import random

def generate_question():
    a = random.randint(-10, 10)
    b = random.randint(-10, 10)
    c = random.randint(-10, 10)

    # Evita que a seja zero para garantir que seja uma função de segundo grau
    while a == 0:
        a = random.randint(-10, 10)

    # Monta a equação
    equation = f"{a}x^2"
    if b >= 0:
        equation += f"+{b}x"
    else:
        equation += f"{b}x"
    if c >= 0:
        equation += f"+{c}"
    else:
        equation += f"{c}"

    # Calcula o delta
    delta = b**2 - 4*a*c

    # Monta a questão
    question = f"Considere a função f(x) = {equation}. Calcule:\n\n"
    question += "a) O valor de delta;\n"
    question += "b) As raízes da função, caso existam;\n"
    question += "c) O valor do vértice da parábola;\n"

    # Monta a resposta
    answer = f"a) Delta = {delta}\n"
    if delta > 0:
        x1 = (-b + delta**0.5) / (2*a)
        x2 = (-b - delta**0.5) / (2*a)
        answer += f"b) As raízes da função são x1 = {x1:.2f} e x2 = {x2:.2f}\n"
    elif delta == 0:
        x = -b / (2*a)
        answer += f"b) A raiz da função é x = {x:.2f}\n"
    else:
        answer += "b) A função não possui raízes reais\n"
    vertex_x = -b / (2*a)
    vertex_y = a*vertex_x**2 + b*vertex_x + c
    answer += f"c) O vértice da parábola é ({vertex_x:.2f}, {vertex_y:.2f})"

    return question, answer

# Gera uma questão e exibe na tela
question, answer = generate_question()
print(question)
print(answer)
