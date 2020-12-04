lista = []
dicionario = {}
mulheres = []
acimaMedia = []
sair = ' '
countPessoas = 0
idades = 0
while True:
    countPessoas += 1
    dicionario['nome'] = str(input('\nNome: ')).strip()
    dicionario['sexo'] = str(input('Sexo: [M/F] ')).strip().upper()[0]
    if dicionario['sexo'] == 'F':
        mulheres.append(dicionario['nome'])
    dicionario['idade'] = int(input('Idade: '))
    lista.append(dicionario.copy())
    idades += dicionario['idade']

    sair = str(input('Desejar sair [S/N] ')).strip().upper()[0]
    if sair in 'S':
        break
    del dicionario['nome']
    del dicionario['sexo']
    del dicionario['idade']

print(f'Foram cadastradas {countPessoas} pessoas')

media = idades / countPessoas
print(f'A idade média das pessoas é {media:.2f}')

print(f'As mulheres cadastradas são {mulheres}')

print(f'E os acima de {media:.2f} são ', end='')
for i in range(0,len(lista)):
    if lista[i]['idade'] > media:
        print(f'{lista[i]["nome"]}', end=' ')
