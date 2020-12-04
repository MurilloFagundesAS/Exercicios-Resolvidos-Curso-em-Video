salario = int(input('Qual o salário do funcionário? '))

if salario <= 1250:
    aumento = salario + (salario * 0.15)
else:
    aumento = salario + (salario * 0.10)
print('O salário era R${:.2f} e agora é R${:.2f}'.format(salario, aumento))