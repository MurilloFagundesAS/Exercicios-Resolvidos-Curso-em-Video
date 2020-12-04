
a = int(input('Digite o valor do primeiro segmento de reta: '))
b = int(input('Digite o valor do segundo segmento de reta: '))
c = int(input('Digite o valor do terceiro segmento de reta: '))


if a < (b+c) and b < (a+c) and c < (a+b):
    if a > abs(b-c) and b > abs(a-c) and c > abs(a-b):
        print('Faz Triângulo!!!')
    else:
        print('Não Faz Triângulo...')
else:
    print('Não Faz Triângulo...')