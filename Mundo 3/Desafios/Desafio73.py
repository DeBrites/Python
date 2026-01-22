# Crie uma tupla preenchida com os 20 primeiros colocados da Tabela do Campeonato Brasileiro de Futebol, na ordem de colocação. 
# Depois mostre: 
# A) Apenas os 5 primeiros colocados.
# B) Os últimos 4 colocados da tabela.
# C) Uma lista com os times em ordem alfabética.
# D) Em que posição na tabela está o time da Chapecoense.
brasileirao2026 = ('Atlético-MG', 'Botafogo', 'Athletico-PR', 'Chapecoense', 
                   'Coritiba', 'Flamengo', 'Vasco da Gama', 'Cruzeiro', 'Bahia', 
                   'EC Vitória', 'Fluminense', 'Grêmio', 'Mirassol', 'Bragantino', 
                   'Remo', 'Santos', 'São Paulo', 'Corinthians', 'Internacional', 'Palmeiras')
print('-=' * 20)
print(f'Lista de times do Brasileirão: {brasileirao2026}')
print('-=' * 20)
print('Os primeiros 5 colocados são: ', brasileirao2026[0:6])
print('-=' * 20)
print('Os últimos 4 colocados são: ', brasileirao2026[-4::])
print('-=' * 20)
print('Os times em ordem alfábetica são: ', sorted(brasileirao2026))
print('-=' * 20)
print(f'O time Chapecoense está na {brasileirao2026.index('Chapecoense') + 1}º posição.')