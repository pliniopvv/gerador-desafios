import random
import numpy as np
from prettytable import PrettyTable

# Criação da tabela
tabela = PrettyTable()

dados = ["0|-20", "20|-40","40|-60","60|-80","80|-100"]
medias = np.array([10, 30, 50, 70, 90])
f = np.array([])
for _ in range(5):
	f=np.append(f, random.randint(1,10))

fi = np.array([])
for v in f:
	fi = np.append(fi, v/sum(f))

fx = np.array([])
for i in range(len(f)):
	fx = np.append(fx, medias[i]*f[i])

media = sum(fx) / sum(f)
variancia = ((medias - media) ** 2) / sum(f)
dp = variancia**0.5

# 
#		PREPARAÇÃO DA APRESENTAÇÃO
#
tabela.field_names = ["X", "f", "fi", "fr" , "X.f", "v", "dp"]

for i in range(len(dados)):
	tabela.add_row([dados[i], f[i], round(fi[i],2), round(fi[i]*100,2), fx[i], round(variancia[i],2), round(dp[i],2)])

tabela.add_row(["Total", sum(f), sum(fi), round(sum(fi*100),2), sum(fx), round(sum(variancia)/sum(f),2), round(sum(dp)/len(f),2)])

# Impressão da tabela
print(tabela)
