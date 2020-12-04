soma = 0
for i in range(1,7):
    x = int(input('Digite um número: '))
    if x % 2 == 0:
        soma = soma + x
print('O valor total foi {}'.format(soma))