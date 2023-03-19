import random

# define as perguntas e respostas
questions = [
    {
        "pergunta": "Uma fábrica produz três tipos de produtos A, B e C, com 20%, 50% e 30% de probabilidade de serem defeituosos, respectivamente. Se 5% dos produtos A, 2% dos produtos B e 3% dos produtos C são selecionados aleatoriamente, qual é a probabilidade de que um produto selecionado aleatoriamente seja defeituoso?",
        "resposta": round(0.2 * 0.05 + 0.5 * 0.02 + 0.3 * 0.03, 4)
    },
    {
        "pergunta": "Uma caixa contém 4 bolas vermelhas, 5 bolas azuis e 6 bolas verdes. Se duas bolas são selecionadas aleatoriamente, sem reposição, qual é a probabilidade de que ambas as bolas sejam vermelhas?",
        "resposta": round(4/15 * 3/14, 4)
    },
    {
        "pergunta": "Um pacote de cartões de presente contém 5 cartões de aniversário e 3 cartões de casamento. Se 2 cartões são selecionados aleatoriamente, sem reposição, qual é a probabilidade de que pelo menos um dos cartões seja de aniversário?",
        "resposta": round(1 - (3/7 * 2/6), 4)
    },
    {
        "pergunta": "Uma loja vende 3 tipos de roupas: camisas, calças e sapatos. A probabilidade de um cliente comprar uma camisa é de 0,4, a probabilidade de comprar uma calça é de 0,3 e a probabilidade de comprar sapatos é de 0,3. A probabilidade de que um cliente compre uma camisa defeituosa é de 0,05, a probabilidade de comprar uma calça defeituosa é de 0,02 e a probabilidade de comprar sapatos defeituosos é de 0,03. Se um cliente compra apenas um item, qual é a probabilidade de que o item seja defeituoso?",
        "resposta": round(0.4 * 0.05 + 0.3 * 0.02 + 0.3 * 0.03, 4)
    },
]

# embaralha as perguntas
random.shuffle(questions)

# itera sobre as perguntas e pede as respostas
score = 0
for q in questions:
    guess = float(input(q["pergunta"] + " "))
    if guess == q["resposta"]:
        print("Resposta correta!")
        score += 1
    else:
        print("Resposta incorreta. A resposta correta é", q["resposta"])

# informa a pontuação final
print("Sua pontuação final é", score, "de", len(questions), "questões.")
