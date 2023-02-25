import random

# Função para gerar um novo desafio
def generate_challenge():
    # Gera dois números aleatórios entre 1 e 99
    a = random.randint(1, 99)
    b = random.randint(1, 99)
    
    # Escolhe se a operação será de soma ou subtração
    op = random.choice(["+", "-"])
    
    # Cria a expressão e calcula o resultado
    if op == "+":
        exp = f"{a} + {b} = "
        res = a + b
    else:
        exp = f"{a} - {b} = "
        res = a - b
    
    # Retorna o desafio e o resultado correto
    return exp, res


# Loop principal do programa
while True:
    # Gera um novo desafio
    challenge, correct_answer = generate_challenge()
    
    # Imprime o desafio e lê a resposta do usuário
    answer = input(challenge)
    
    # Verifica se a resposta está correta
    if int(answer) == correct_answer:
        print("Resposta correta!")
    else:
        print("Resposta incorreta.")
    
    # Pula uma linha para o próximo desafio
    print()
