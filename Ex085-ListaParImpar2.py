lista = [[], []]

for i in range(0,7):
    x = int(input(f'Digite o {i+1}º número: '))

    if x % 2 == 0:
        lista[0].append(x)
    else:
        lista[1].append(x)

lista[0].sort()
lista[1].sort()
print(f'Os números digitados foram: {lista}')
print(f'Os pares são: {lista[0]}')
print(f'Os impares são: {lista[1]}')