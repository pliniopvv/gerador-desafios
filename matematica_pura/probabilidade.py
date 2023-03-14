import random

# define as perguntas e respostas
questions = {
    "Qual é a probabilidade de jogar um dado e obter um número par? (em porcentagem)": "50",
    "Uma urna contém 6 bolas vermelhas e 4 bolas azuis. Qual é a probabilidade de escolher uma bola vermelha? (em porcentagem)": "60",
    "Qual é a probabilidade de escolher duas cartas de um baralho de 52 cartas e obter duas cartas de espadas? (em porcentagem)": "5.9",
    "Uma urna contém 10 bolas numeradas de 1 a 10. Qual é a probabilidade de escolher uma bola com um número menor que 5? (em porcentagem)": "40",
    "Um grupo de 20 pessoas inclui 12 homens e 8 mulheres. Qual é a probabilidade de escolher duas pessoas ao acaso e ambas serem mulheres? (em porcentagem)": "14.3",
    "Qual é a probabilidade de jogar duas moedas e obter duas caras? (em porcentagem)": "25",
    "Um saco contém 8 bolas vermelhas e 4 bolas azuis. Qual é a probabilidade de escolher duas bolas sem reposição e obter duas bolas vermelhas? (em porcentagem)": "28.6",
    "Qual é a probabilidade de escolher aleatoriamente um número de 1 a 10 que seja ímpar? (em porcentagem)": "50",
}

# embaralha as perguntas
questions = list(questions.items())
random.shuffle(questions)

# itera sobre as perguntas e pede as respostas
score = 0
for q, a in questions:
    guess = input(q + " ")
    if guess == a:
        print("Resposta correta!")
        score += 1
    else:
        print("Resposta incorreta. A resposta correta é", a + ".")

# informa a pontuação final
print("Sua pontuação final é", score, "de", len(questions), "questões.")
