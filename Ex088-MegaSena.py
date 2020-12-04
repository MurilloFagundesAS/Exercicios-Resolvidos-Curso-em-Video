from random import randint
from time import sleep
todosPalpites = []
palpite = []

jogos = int(input('Quantos palpites você deseja? '))

for i in range(0, jogos):
    for j in range(0,6):
        x = randint(1,60)
        if x not in palpite:
            palpite.append(x)
        else:
            while x in palpite:
                x = randint(1,60)
            palpite.append(x)

    palpite.sort()
    todosPalpites.append(palpite[:])
    palpite.clear()

print('Os Palpites São:')
for i in range(0, jogos):
    sleep(1)
    print(f'{i+1}º palpite: {todosPalpites[i]}')