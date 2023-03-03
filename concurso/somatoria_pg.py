import random

def soma_pg(a1, r, n):
    return a1 * ((1 - r**n) / (1 - r))

# Gera uma questão aleatória
def gerar_questao():
    a1 = random.randint(1, 10)
    r = random.randint(2, 5)
    n = random.randint(2, 5)
    soma = soma_pg(a1, r, n)
    return f"Qual é a soma dos {n} primeiros termos da P.G. de primeiro termo {a1} e razão {r}?"

# Recebe a resposta do usuário e verifica se está correta
def verificar_resposta(questao, resposta):
    a1 = int(questao.split()[9])
    r = int(questao.split()[14])
    n = int(questao.split()[6])
    soma = soma_pg(a1, r, n)
    if float(resposta) == soma:
        return True
    else:
        return False

# Exibe a questão e recebe a resposta do usuário
def fazer_questao():
    questao = gerar_questao()
    print(questao)
    resposta = input("Resposta: ")
    if verificar_resposta(questao, resposta):
        print("Parabéns, você acertou!")
    else:
        print("Ops, resposta incorreta. Tente novamente.")

# Executa o programa
fazer_questao()
