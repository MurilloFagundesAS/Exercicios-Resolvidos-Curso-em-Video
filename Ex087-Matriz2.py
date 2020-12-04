lista = []
parte = []
par = 0
coluna3 = 0
count = 0
maior = 0

for i in range(0,3):
    for j in range(0,3):
        x = int(input(f'Digite um número da posição [{i},{j}]: '))
        if x % 2 ==0:
            par += x
        if j == 2:
            coluna3 += x
        parte.append(x)
    if count == 0:
        maior = x
        count += 1
    if x > maior and i == 1:
        maior = x
    lista.append(parte[:])
    parte.clear()

for i in range(0,3):
    for j in range(0,3):
        print(f'[{lista[i][j]}] ', end='')
    print()
print(f'A soma dos valores pares é {par}')
print(f'A soma da 3ª coluna é {coluna3}')
print(f'E o maior número da segunda linha é {maior}')