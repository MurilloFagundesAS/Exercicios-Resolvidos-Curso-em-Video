print('{:=^30}'.format(' MERCADO '))

total = 0
maisQuemil = 0
barato = 0
nomeBarato = ''
contagem = 0
while True:
    nome = str(input('Nome do produto: ')).strip().upper()
    preco = float(input('Preço: '))

    total += preco

    if preco > 1000:
        maisQuemil += 1

    if contagem < 1:
        nomeBarato = nome
        barato = preco
        contagem += 1
    if preco < barato:
        nomeBarato = nome

    fim = str(input('Algo mais? [S/N] ')).strip().upper()
    if fim == 'N':
        break
print(f'A compra deu R${total:.2f}')
print(f'Itens acima de R$1000,00 = {maisQuemil}')
print(f'Item mais barato = {nomeBarato}')
print('{:=^30}'.format(' FIM '))