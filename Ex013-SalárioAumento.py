x = float(input('Qual o valor do salário? '))

aumento = x + (x*0.15)

print('O salário era R${:.2f}, mas\nagora com 15% de aumento\né de R${:.2f}'.format(x, aumento))