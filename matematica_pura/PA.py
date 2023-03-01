import random

# Gera uma questão sobre PA com n termos e razão r
def gerar_questao(n, r):
    termo_inicial = random.randint(1, 20)
    pa = [termo_inicial + (i-1)*r for i in range(1, n+1)]
    resposta = pa[-1] + r
    return f"Qual é o próximo termo da PA: {pa}? ", resposta

# Gera 5 questões com 10 termos e razão 3
for i in range(5):
    questao, resposta = gerar_questao(10, 3)
    print(f"Questão {i+1}: {questao}")
    tentativa = int(input("Resposta: "))
    if tentativa == resposta:
        print("Parabéns, você acertou!\n")
    else:
        print(f"Resposta incorreta. O valor correto é {resposta}.\n")
