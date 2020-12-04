from time import sleep
lista = []
sair = ' '

while True:
    nome = str(input('Digite o nome do aluno: ')).strip()
    nota1 = float(input('Digite a primeira nota: '))
    nota2 = float(input('Digite a segunda nota: '))
    media = (nota1 + nota2) / 2
    lista.append([nome, [nota1, nota2], media])

    sair = str(input('Deseja sair: [S/N] ')).upper().strip()
    if sair in 'S':
        break

print('{:=^27}'.format(' BOLETIM '))
print('{:<5}{:^12}{:>10}'.format('Nº', 'NOME', 'MÉDIA'))
print('='*27)
for i in range(0, len(lista)):
    print(f'{i:<5}{lista[i][0]:^12}{lista[i][2]:>10.2f}')
print('='*27)

while True:
    mostrar = int(input('Digite o número do aluno \npara mostrar suas notas:\n[Digite 999 para sair] '))
    if mostrar == 999:
        break
    for i in range(0, len(lista)):
        if i == mostrar:
            print(f'{lista[i][0]} tirou {lista[i][1]}')
        elif i not in lista:
            print('Aluno não cadastrado!')
    print('='*27)
    sleep(2)
print('{:=^27}'.format(' FIM '))
