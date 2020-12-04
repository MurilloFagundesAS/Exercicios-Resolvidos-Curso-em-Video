from time import sleep
lista = []
sair = ' '
count = 0
while True:
    lista.append(int(input('Digite um \33[31mvalor\33[m: ')))
    count += 1

    sair = str(input('Deseja sair? [S/N] ')).upper().strip()
    if sair in 'S':
        break
print('Fim do recebimento de dados!\nO Pc agora está processando...')
sleep(1)
print(lista)

print(f'Foram digitados \33[31m{count}\33[m números!')
sleep(1)

lista.sort(reverse=True)
print(f'A lista em ordem decrescente é: {lista} !')
sleep(1)

if lista.count(5) == 0:
    print('O valor \33[31m5\33[m não foi digitado...')
else:
    print(f'O valor \33[31m5\33[m foi digitado \33[31m{lista.count(5)}\33[m vezes!')
