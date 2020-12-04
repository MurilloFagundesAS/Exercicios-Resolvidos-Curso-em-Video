x = 'S'
contmedia = 0
soma = 0
maior = 0
menor = 0
condicao = 1
while x == 'S':
    n = int(input('Digite um número: '))
    soma += n
    contmedia += 1
    x = str(input('Digite S para continuar: ')).strip().upper()

    if condicao == 1:
        maior += n
        menor += n
        condicao += 1

    if n > maior:
        maior = n

    if n < menor:
        menor = n

media = soma / contmedia
print(f'A \33[31mmédia\33[m é \33[31m{media:.2f}\33[m!')
print(f'O \33[31mmaior\33[m número é \33[31m{maior:.2f}\33[m!')
print(f'O \33[31mmenor\33[m número é \33[31m{menor:.2f}\33[m!')