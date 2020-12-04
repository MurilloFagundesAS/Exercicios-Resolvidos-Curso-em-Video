lista = []
parte = []

for i in range(0,3):
    for j in range(0,3):
        x = int(input(f'Digite um número da posição [{i},{j}]: '))
        parte.append(x)
    lista.append(parte[:])
    parte.clear()

for i in range(0,3):
    for j in range(0,3):
        print(f'[{lista[i][j]}] ', end='')
    print()
