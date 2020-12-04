lista = []
for i in range(0,5):
    lista.append(int(input(f'Digite o \33[31mvalor\33[m da posição {i}: ')))
print(lista)

print(f'O \33[31mmaior\33[m valor foi \33[31m{max(lista)}\33[m que encontra-se na(s) posição(ões): ', end='')
for i in range(0, len(lista)):
    if lista[i] == max(lista):
        print(f'{lista.index(lista[i], i)} ', end="")

print(f'\nE o \33[31mmenor\33[m valor foi \33[31m{min(lista)}\33[m que se encontra na(s) posição(ões): ', end='')
for i in range(0, len(lista)):
    if lista[i] == min(lista):
        print(f'{lista.index(lista[i], i)} ', end='')
