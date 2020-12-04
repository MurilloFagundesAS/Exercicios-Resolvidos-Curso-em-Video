import math

n = float(input('Digite um número real qualquer: '))

a = math.floor(n)

print('O número {} arredondado é {}'.format(n, math.trunc(n))) #trunc só mostra a parte inteira
print('O número x arredondado é {:.0f}'.format(n)) #int só mostra a parte inteira
#:.0f arredonda o valor normalmente