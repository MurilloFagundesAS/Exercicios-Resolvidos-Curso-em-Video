lista = []
par = []
impar = []
sair = ' '
while True:
    lista.append(int(input('Digite um número: ')))


    sair = str(input('Deseja sair? [S/N] ')).upper().strip()
    if sair in 'S':
        break
print(f'Lista Original: {lista}')

for i in range(0, len(lista)):
    if lista[i] % 2 == 0:
        par.append(lista[i])
    else:
        impar.append(lista[i])

print(f'Lista de Pares: {par}')
print(f'Lista de Impares: {impar}')