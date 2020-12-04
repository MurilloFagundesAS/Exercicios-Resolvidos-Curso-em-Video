dicionario = {}
lista = []

nome = str(input('\nQual o nome do jogador? ')).strip()
dicionario['nome'] = nome
partidas = int(input(f'Quantas partidas {nome} jogou? '))

for i in range(1, partidas+1):
    gols = int(input(f'Quantos gols ele fez na partida {i}? '))
    lista.append(gols)
dicionario['gols'] = lista[:]

total = 0
for i in range(0, len(lista)):
    total += lista[i]
dicionario['total'] = total

print('=-'*30)
print(dicionario)
print('=-'*30)

for k, v in dicionario.items():
    print(f'O campo {k} tem {v}')
print('=-'*30)

print(f'O jogador {nome} jogou {partidas} partidas e nelas fez:')
for i in range(0, len(lista)):
    print('{:>5} Na partida {} fez {} gols'.format('==>', i+1,lista[i]))
print(f'Tendo um total de {total} gols')
print('=-'*30)