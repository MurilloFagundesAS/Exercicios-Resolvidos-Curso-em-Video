from random import randint
tupla = (randint(1,10), randint(1,10), randint(1,10), randint(1,10), randint(1,10))
'''a = randint(1,9)
b = randint(1,9)
c = randint(1,9)
d = randint(1,9)
e = randint(1,9)
tupla = (a,b,c,d,e)'''
print(f'Os valores sorteados foram: {tupla}')
print(f'O maior é {max(tupla)}')
print(f'O menor é {min(tupla)}')

'''maior = 0
menor = 0
for i in range(0,5):
    if i == 0:
        maior = tupla[i]
        menor = tupla[i]
    if tupla[i] > maior:
        maior = tupla[i]
    if tupla[i] < menor:
        menor = tupla[i]
print(f'O \33[31mmaior\33[m número foi: \33[31m{maior}\33[m')
print(f'O \33[31mmenor\33[m número foi: \33[31m{menor}\33[m')'''