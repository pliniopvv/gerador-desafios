import os
import random

# Diretório que contém os arquivos
diretorio = "/home/gangss/Documentos/@/Python/exercicios/concurso/"

# Lista todos os arquivos no diretório
arquivos = os.listdir(diretorio)

# Seleciona um arquivo aleatoriamente
arquivo_selecionado = random.choice(arquivos)

# Executa o arquivo selecionado como um script Python
#os.system("python " + diretorio + "/" + arquivo_selecionado)
print(arquivo_selecionado)
