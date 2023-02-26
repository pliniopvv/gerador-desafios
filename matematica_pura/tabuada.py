import random

# Função para gerar perguntas
def perguntar(num1, num2):
    resposta_correta = num1 * num2
    resposta_usuario = int(input(f"{num1} x {num2} = "))
    if resposta_usuario == resposta_correta:
        print("Parabéns, resposta correta!")
        return True
    else:
        print(f"Resposta incorreta! R: {resposta_correta}.")
        return False

# Configurações iniciais
tabuada = list(range(1, 11))
acertos = 0
erros = 0

# Laço para gerar perguntas aleatórias
while True:
    num1 = random.choice(tabuada)
    num2 = random.choice(tabuada)
    acertou = perguntar(num1, num2)
    
    # Atualiza os acertos e erros
    if acertou:
        acertos += 1
    else:
        erros += 1
    
    # Verifica se o usuário quer continuar
#    continuar = input("Deseja continuar? (S/N)").upper()
#    if continuar == "N":
#        break

# Exibe o resultado final
#print(f"Você acertou {acertos} e errou {erros} questões.")
