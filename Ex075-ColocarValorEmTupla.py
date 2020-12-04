tupla = (int(input('Digite um número: ')),
         int(input('Digite um número: ')),
         int(input('Digite um número: ')),
         int(input('Digite um número: ')))


'''print('='*35)
a = int(input('Digite o primeiro valor: '))
b = int(input('Digite o segundo valor: '))
c = int(input('Digite o terceiro valor: '))
d = int(input('Digite o quarto valor: '))
tupla = (a, b, c, d)
print(tupla)


if tupla.count(9) >=1:
    print(f'O valor \33[31m9\33[m aparece \33[31m{tupla.count(9)}\33[m vezes')
else:
    print(f'O valor \33[31m9 NÃO\33[m apareceu')

if tupla.count(3) >=1:
    x = tupla.index(3)
    print(f'O primeiro \33[31m3\33[m aparece na posição \33[31m{x+1}\33[m')
else:
    print(f'O valor \33[31m3 NÃO\33[m apareceu')

count = 0
for i in range(0,4):
    if tupla[i] % 2 == 0:
        count +=1
if count >= 1:
    print(f'E os números \33[31mpares\33[m foram: ', end='')
    for i in range(0, 4):
        if tupla[i] % 2 == 0:
            print(f'{tupla[i]} ', end='')
else:
    print(f'\33[31mNÃO\33[m há números \33[31mpares\33[m', end='')

print()
print('='*35)'''