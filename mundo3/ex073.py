times = ('Internacional', 'São Paulo', 'Atlético-MG', 'Vasco',
         'Flamengo', 'Palmeiras', 'Santos', 'Fluminense',
         'Sport', 'Ceará', 'Corinthians', 'Bahia',
         'Fortaleza', 'Grêmio', 'Botafogo', 'Athletico-PR',
         'Coritiba', 'Atlético-GO', 'Bragantino', 'Goiás')
print('-=' * 15)
print(f'Lista de times: {times}')
print('-=' * 15)
print(f'Os 5 primeiros colocados são: {times[0:5]}')
print('-=' * 15)
print(f'Os 4 últimos colocados são: {times[-4:]}')
print('-=' * 15)
print(f'Times em ordem alfabética: {sorted(times)}')
print('-=' * 15)
print(f'O Flamengo está na {times.index("Flamengo")+1}ª posição')
