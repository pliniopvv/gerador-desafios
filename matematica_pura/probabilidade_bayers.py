import random

prob_A = random.uniform(0.01,0.09)
prob_B = random.uniform(0.5,0.90)
prob_nA_dado_B = random.uniform(0.01,0.10)

#prob_A = 0.01 # têm câncer
#prob_B = 0.8 # dá positivo
#prob_nA_dado_B = 0.09 # não tem câncer, porém dá resultado positivo.
# Resultado é 0.082 conferido.

question = f"""
Imaginemos que o teste de mamografia se comporte da seguinte forma:
- {prob_A*100:.2f}% das mulheres têm cancer de mama
- {prob_B*100:.2f}% das mamografias detectam o câncer quando ele existe
- {prob_nA_dado_B*100:.2f}% das mamografias detectam o câncer quando ele não existe.
        Qual é a probabilidade de uma mulher com resultado positivo tenha de fato câncer?
"""

print(question)
resposta = input("Resposta: ")

prob_nA = 1 - prob_A
prob_nB = 1 - prob_B
prob_nAdnB = 1 - prob_nA_dado_B

teoremadebayes = (prob_A * prob_B) / ( prob_A * prob_B + prob_nA * prob_nA_dado_B )

if (float(resposta) - teoremadebayes <= 0.001):
    print("Resposta correta!")
else:
    print("Resposta incorreta! R: ",teoremadebayes)