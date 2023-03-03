import random

# Função que gera uma PA aleatória
def gerar_pa():
    a1 = random.randint(1, 10)  # Primeiro termo da PA
    r = random.randint(1, 10)  # Razão da PA
    n = random.randint(3, 7)   # Número de termos da PA
    return [a1 + i * r for i in range(n)], r

# Função que calcula a soma dos termos de uma PA
def soma_pa(a1, r, n):
    return (n * (2 * a1 + (n - 1) * r)) / 2

# Loop principal do programa
while True:
    pa, r = gerar_pa()
    a1, an = pa[0], pa[-1]
    n = len(pa)
    soma = soma_pa(a1, r, n)
    
    # Exibe a pergunta
    print("Qual é a soma dos termos da seguinte PA:")
    print(pa)
    
    # Lê a resposta do usuário
    resposta = float(input("Resposta: "))
    
    # Verifica se a resposta está correta
    if resposta == soma:
        print("Resposta correta!")
    else:
        print("Resposta incorreta. A soma dos termos é", soma)
    
    # Pede para o usuário pressionar Enter para continuar
    input("Pressione Enter para continuar...")
