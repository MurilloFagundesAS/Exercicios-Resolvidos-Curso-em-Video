times = ('Flamengo', 'Santos', 'Palmeiras', 'Grêmio', 'Atlético-PR', 'São Paulo',
         'Internacional', 'Corinthias', 'Fortaleza', 'Goiás', 'Bahia', 'Vasco da Gama',
         'Atlético-MG', 'Fluminense', 'Bota-Fogo', 'Ceará SC', 'Cruzeiro', 'CSA',
         'Chapecoense', 'Avaí')

print(f'Os primeiros 5 colocados do Brasileirão são: {times[0:5]}')
print(f'Os últimos 4 colocados do Brasileirão são: {times[16:21]}')
print(f'Os times do Brasileirão em ordem alfabética: {sorted(times)}')
x = times.index('Chapecoense')
print(f'A Chapecoense está na {times.index("Chapecoense")}º posição')  # Aspas dupla pra
                                                                    # evitar Interpolação
