a = int(input('Digite o valor do primeiro segmento de reta: '))
b = int(input('Digite o valor do segundo segmento de reta: '))
c = int(input('Digite o valor do terceiro segmento de reta: '))


if a < (b+c) and b < (a+c) and c < (a+b):
    if a > abs(b-c) and b > abs(a-c) and c > abs(a-b):
        print('Faz Triângulo!!!')
        if (a == b) and (a == c) and (b==c):
            print('O Triângulo, no caso, é EQUILATERO!')
        elif (a == b) and (a!=c) or (b==c) and (b!=a) or (c==a) and (c!=b):
            print('O Triângulo, no caso, é ISÓCELES!')
        elif a!=b and a!=c and b!=c:
            print('O Triângulo, no caso, é ESCALENO!')
    else:
        print('Não Faz Triângulo...')
else:
    print('Não Faz Triângulo...')