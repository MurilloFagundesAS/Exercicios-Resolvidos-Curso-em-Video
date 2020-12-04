from random import randint
from time import sleep

numeros = []
def sorteio():
    for j in range(0,5):
        x = randint(1, 10)
        numeros.append(x)

def somaPar():
    soma = 0
    for i in range (0,5):
        if numeros[i]%2 == 0:
            soma += numeros[i]
    print(f'\33[31m{soma}\33[m')

print('Os números sorteados são: ', end='')
for i in range (0,5):
    print(f'{numeros[i]} ', end='')
    sleep(1)

print('E a soma dos Pares é: ', end= '')
somaPar()