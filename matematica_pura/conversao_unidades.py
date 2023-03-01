import random

# Dicionário de unidades e seus respectivos símbolos
unidades = {
    'metro': 'm',
    'quilômetro': 'km',
    'centímetro': 'cm',
    'milímetro': 'mm',
    'quilate': 'ct',
    'grama': 'g',
    'quilograma': 'kg',
    'tonelada': 't',
    'segundo': 's',
    'minuto': 'min',
    'hora': 'h',
    'dia': 'd',
}

# Lista de fatores de conversão
fatores = [
    ('metro', 'quilômetro', 0.001),
    ('metro', 'centímetro', 100),
    ('metro', 'milímetro', 1000),
    ('quilate', 'grama', 0.2),
    ('grama', 'quilograma', 0.001),
    ('quilograma', 'tonelada', 0.001),
    ('segundo', 'minuto', 0.0166667),
    ('minuto', 'hora', 0.0166667),
    ('hora', 'dia', 0.0416667),
]

# Função que gera uma questão aleatória
def gerar_questao():
    unidade1, simbolo1 = random.choice(list(unidades.items()))
    unidade2, simbolo2 = random.choice(list(unidades.items()))
    fator = 1
    while fator == 1:
        unidade1, simbolo1 = random.choice(list(unidades.items()))
        unidade2, simbolo2 = random.choice(list(unidades.items()))
        fator = next((f[2] for f in fatores if f[0] == unidade1 and f[1] == unidade2), 1)
    valor = random.randint(1, 1000)
    resposta = round(valor * fator, 2)
    return f'Qual o valor de {valor} {simbolo1} em {unidade2}?', resposta

# Função principal que gera e apresenta as questões
def main():
    acertos = 0
    while True:
        questao, resposta_correta = gerar_questao()
        resposta_usuario = input(f'{questao} ')
        if resposta_usuario.lower() == 'sair':
            break
        try:
            resposta_usuario = float(resposta_usuario)
        except ValueError:
            print('Resposta inválida. Tente novamente.')
            continue
        if resposta_usuario == resposta_correta:
            acertos += 1
            print('Resposta correta!')
        else:
            print(f'Resposta incorreta. A resposta correta era {resposta_correta} {unidades[unidade2]}.')
    print(f'Você acertou {acertos} questões.')


main()
