'''
Crie uma tupla preenchida com os 20 primeiros colocados da tabela do Campeonato Brasileiro de Futebol, na orde de colocação. Depois mostre:

A) Apenas os 5 priemiros colocados.
B) Os últimos 4 colocados da tabela.
C) Uma lista com os times em ordem alfabética
D) Em que posição da tablea está o time do Botafogo
'''
times = ('Santos', 'Atlético Mineiro', 'Corinthians', 'Cuiabá Saf', 'Internacional', 'Avaí', 'Red Bull Bragantino', 'Palmeiras', 'Flamengo', 'Coritiba', 'São Paulo', 'Botafogo', 'Fluminense', 'América Fc Saf', 'Ceará', 'Athletico Paranaense', 'Atlético', 'Goiás', 'Juventude', 'Fortaleza')

print(f'Os 5 primeiros colocados são {times[0:5]}')
print('-=' * 5)
print(f'Os últimos 4 colocados são {times[-4:]}')
print('-=' * 5)
print(f'Em ordem alfabetica: {sorted(times)}')
print('-=' * 5)
print(f'O Botafogo está na {times.index("Botafogo")+1}ª posição ')

