x = float(input('Qual o valor do produto? '))

desconto = x - (x*0.05)

print('O produto vale R${:.2f}, mas está saindo\npor R${:.2f} devido a 5% de desconto'.format(x, desconto))