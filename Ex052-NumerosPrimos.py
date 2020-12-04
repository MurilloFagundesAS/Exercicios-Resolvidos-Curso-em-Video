n = int(input('Digite um número: '))

primo = 0
for i in range(1,n+1):
    if n % i == 0:
        primo += 1

if primo > 2:
    print(f'o número \33[31m{n}\33[m \33[1mNÃO\33[m é um número primo')
    print(f'Ele é divisivel por: ', end="")
    for i in range(1, n + 1):
        if n % i == 0:
            print(f'\33[31m{i}\33[m', end=' ')
        else:
            print(f'{i}', end=" ")
else:
    print(f'o número \33[31m{n}\33[m \33[1mÉ\33[m um número primo')
    print(f'Ele é divisivel por: ', end="")
    for i in range (1, n+1):
        if n % i ==0:
            print(f'\33[31m{i}\33[m', end=' ')
        else:
            print(f'{i}', end=" ")
