pessoas = []
dados = list()
sair = ' '
count = 0
maior = 0
menor = 0

while True:
    dados.append(str(input('Qual o Nome? ')))
    dados.append(int(input('Qual o Peso? ')))
    count += 1

    pessoas.append(dados[:])

    dados.clear()
    sair = str(input('Deseja sair [S/N] ')).strip().upper()
    if sair in 'S':
        break
print(f'Dados das pessoas cadastradas: {pessoas}')
print(f'Foram cadastradas {count} pessoas')

count = 0
for peso in pessoas:
    if count == 0:
        maior = peso[1]
        menor = peso[1]
        count += 1
    if peso[1] >= maior:
        maior = peso[1]
    if peso[1] <= menor:
        menor = peso[1]

print(f'O maior peso foi {maior:.2f}Kg e as pessoas mais pesadas são: ', end='')
for nome in pessoas:
    if nome[1] == maior:
        print(f'{nome[0]} ', end='')

print(f'\nO menor peso foi {menor:.2f}Kg e as pessoas mais leves são: ', end='')
for nome in pessoas:
    if nome[1] == menor:
        print(f'{nome[0]} ', end='')
