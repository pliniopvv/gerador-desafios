import random

# lista de pronomes relativos
relativos = ["que", "quem", "cujo", "cujos", "cuja", "cujas", "onde"]

# lista de frases para usar como exemplo
frases = [
    "O livro _____ você leu é muito bom.",
    "O menino _____ ganhou o prêmio é meu amigo.",
    "O carro _____ eu comprei é vermelho.",
    "O computador _____ você usou estava lento.",
    "O parque _____ nós visitamos era muito bonito.",
    "O professor _____ ensina matemática é muito competente.",
    "A escola _____ você estudou fica longe daqui."
]

# função para gerar questão aleatória
def gerar_questao():
    # escolhe uma frase aleatória
    frase = random.choice(frases)
    # escolhe um pronome relativo aleatório
    relativo = random.choice(relativos)
    # preenche a frase com o pronome relativo
    questao = frase.replace("_____", relativo)
    # retorna a questão e o pronome relativo
    return (questao, relativo)

# exemplo de uso
questao, relativo = gerar_questao()
print("Complete a frase com um pronome relativo:\n")
print(questao)
resposta = input("\nQual é o pronome relativo que completa a frase? ")
if resposta.lower() == relativo:
    print("\nResposta correta!")
else:
    print("\nResposta incorreta. A resposta correta é:", relativo)
