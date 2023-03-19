import random
import math

n = random.randint(4,10)
p = random.randint(1,n-1)
s = random.uniform(0.4,0.9)
q = 1 - s

#n = 6
#p = 2
#s = 0.8
#q = 1 - s
# resultado : 0.01536

def DB(n,p,s,q):
    return C(n,p)*(s**p)*(q**(n-p))

def C(n,p):
    return math.factorial(n) / (math.factorial(n-p)*math.factorial(p))

question = f"""
Um inspetor de qualidade extrai uma amostra de {n} tubos aleatoriamente de uma carga muito grande de tubos que se sabe que contém {q*100:.2f}% de tubos defeituosos. Qual é a probabilidade de pelo menos {p} dos tubos extraídos sejam defeituosos?
"""

print(question)
r = float(input("Resposta: "))
c = DB(n,p,s,q)

if (c - r <= 0.0001):
    print("Resposta correta!")
else:
    print("Resposta incorreta! R:", c ) 