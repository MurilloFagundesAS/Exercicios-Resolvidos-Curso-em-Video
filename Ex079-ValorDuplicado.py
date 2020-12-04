valores = []
sair = ' '
while True:
    x = int(input('Acrescente um valor a lista: '))
    if x in valores:
        print('Valor Duplicado! Não irei adicioná-lo a lista...')
    else:
        valores.append(x)
        print('Valor adicionado com sucesso!')

    sair = (str(input('Deseja sair: [S/N] '))).upper().strip()
    if sair in 'S':
        break
print(valores)
