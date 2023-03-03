import random

def gerar_questao():
    # Gerando números aleatórios para a questão
    p = random.randint(100, 1000)
    r = random.randint(1, 10)
    t = random.randint(1, 5)
    
    # Calculando a resposta
    juros = p * r * t / 100
    resposta = round(juros, 2)
    
    # Criando a questão
    questao = f"Qual é o juro simples de {p} reais a uma taxa de {r}% ao mês durante {t} meses?"
    
    return questao, resposta

def verificar_resposta(questao, resposta):
    # Pedindo ao usuário para inserir a resposta
    tentativa = input(f"{questao} Resposta: ")
    
    # Verificando se a resposta está correta
    if tentativa == str(resposta):
        print("Resposta correta!")
    else:
        print(f"Resposta incorreta. A resposta correta é {resposta}.")

# Gerando a questão e verificando a resposta
questao, resposta = gerar_questao()
verificar_resposta(questao, resposta)
