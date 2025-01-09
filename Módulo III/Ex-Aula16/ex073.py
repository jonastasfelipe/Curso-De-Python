# Crie uma tupla preenchida com os 20 primeiros colocados da Tabela do Campeonato Brasileiro de Futebol, na ordem de colocação. Depois mostre:
# a) Os 5 primeiros times.
# b) Os últimos 4 colocados.
# c) Times em ordem alfabética. 
# d) Em que posição está o time da Chapecoense.
print('-'*37)
print('Tabela do Campeonato Brasileiro 2024')
print('-'*37)
times = ('Botafogo', 'Palmeiras', 'Flamengo', 'Fortaleza', 'Internacional', 'São Paulo', 'Corinthians', 'Bahia', 'Cruzeiro', 'Vasco da Gama', 'Vitória', 'Atlético Mineiro', 'Fluminense', 'Grêmio', 'Juventude', 'Red Bull Bragantino', 'Athletico Paranaense', 'Criciúma', 'Atletico Goianiense', 'Cuiabá')
print('*-*'*50)
print(f'Os 5 primeiros colocados são: {times[0:5]}\n')
print('*-*'*50)
print(f'Os 4 últimos colocados são: {times[-4:]}\n')
print('*-*'*50)
print(f'Times em ordem alfabética: {sorted(times)}\n')
print('*-*'*50)
print(f'O Criciúma está na {times.index("Criciúma")+1}ª posição\n')
print('*-*'*50)