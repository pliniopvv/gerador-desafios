import random
import math

def arranjo(n, k):
    return math.factorial(n) / math.factorial(n-k)

def combinacao(n, k):
    return math.factorial(n) / (math.factorial(k) * math.factorial(n-k))

def permutacao(n):
    return math.factorial(n)

print("Escolha o tipo de cálculo que deseja praticar:")
print("1 - Arranjo")
print("2 - Combinação")
print("3 - Permutação")
opcao = input("Digite sua opção: ")

if opcao == "1":
    n = random.randint(1, 10)
    k = random.randint(1, n)
    resposta = input("Qual o arranjo de {} elementos tomados {} a {}? ".format(n, k, k))
    correta = arranjo(n, k)
elif opcao == "2":
    n = random.randint(1, 10)
    k = random.randint(1, n)
    resposta = input("Qual a combinação de {} elementos tomados {} a {}? ".format(n, k, k))
    correta = combinacao(n, k)
elif opcao == "3":
    n = random.randint(1, 10)
    resposta = input("Qual a permutação de {} elementos? ".format(n))
    correta = permutacao(n)
else:
    print("Opção inválida.")

if resposta == str(correta):
    print("Resposta correta!")
else:
    print("Resposta incorreta. A resposta correta é {}.".format(correta))
