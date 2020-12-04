from random import randint
from time import sleep
dicionario = dict()

for i in range(0,4):
    dado = randint(1,6)
    print(f'O jogador{i+1} rolou um {dado}')

    dicionario[i] = dado
    sleep(1)

lista = sorted(dicionario.values(), reverse=True)
print(dicionario)
print(lista)

for i in range(0,4):
    if dicionario[i] == lista[i]:
        print(f'{i+1}º LUGAR: Jogador tirou {lista[i]}')