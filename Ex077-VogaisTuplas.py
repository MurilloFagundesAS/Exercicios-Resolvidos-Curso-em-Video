from time import sleep
tupla = ('Murillo', "Edileuza", 'Laila', 'Odair')

'''for vogal in tupla:
    print(f'A palavra \33[31m{vogal}\33[m tem as vogais: ', end='')
    if 'A' in vogal or 'a' in vogal:
        print(f'A', end=' ')
    if 'E' in vogal or 'e' in vogal:
        print(f'E', end=' ')
    if 'I' in vogal or 'i' in vogal:
        print(f'I', end=' ')
    if 'O' in vogal or 'o' in vogal:
        print(f'O', end=' ')
    if 'U' in vogal or 'u' in vogal:
        print(f'U', end=' ')
    print()
    sleep(1)'''

for vogal in tupla:
    print(f'\nA palavra \33[31m{vogal}\33[m tem as vogais: ', end='')
    for letra in vogal:
        if letra.upper() in 'AEIOU':
            print(f'{letra} ', end='')