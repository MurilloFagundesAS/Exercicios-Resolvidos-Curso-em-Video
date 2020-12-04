print('{:=^40}'.format('Murillo'))
preco = float(input('Qual preço NORMAL do produto? '))

pgmt = int(input('Qual a forma de pagamento:\n'
                 '1 - À Vista no Dinheiro ou Cheque\n'
                 '2 - À Vista no Cartão, com 5% de Desconto\n'
                 '3 - Em 2x no Cartão, preço normal\n'
                 '4 - Em 3x ou mais no Cartão, com 20% de Juros\n'))
if pgmt == 1:
    print('O produto sai por R${:.2f} à vista'.format(preco))
elif pgmt == 2:
    desconto = preco - (preco*0.05)
    print('O produto de R${} sai por R${:.2f} devido a 5% de desconto'.format(preco, desconto))
elif pgmt == 3:
    print('O produto sai por R${:.2f} em 2x no Cartão'.format(preco))
else:
    juros = preco + (preco*0.20)
    print('O produto de R${} sai por R${} devido a 20% de juros'.format(preco,juros))