from time import sleep
n1 = float(input('Digite o 1º valor: '))
n2 = float(input('Digite o 2º valor: '))

sair = 0
while sair != 5:
    print('''
    MENU
    Digite:
    
    [ 1 ] Para somar
    [ 2 ] Para multiplicar
    [ 3 ] Para saber qual é o maior
    [ 4 ] Para entrar com novos números
    [ 5 ] Para sair''')
    sair = int(input())
    if sair == 1:
        conta = n1 + n2
        print('A soma de {:.2f} + {:.2f} = {:.2f}'.format(n1,n2,conta))
        sleep(1)
    if sair == 2:
        conta = n1 * n2
        print('A multiplicação de {:.2f} x {:.2f} = {:.2f}'.format(n1,n2,conta))
        sleep(1)
    if sair == 3:
        if n2<n1:
            maior = n1
            n1 = n2
            n2 = maior
            print('O maior é {:.2f} e o menor {:.2f}')
            sleep(1)
        else:
            print('O maior é {:.2f} e o menor {:.2f}'.format(n1,n2))
            sleep(1)
    if sair == 4:
        n1 = float(input('Digite o novo valor do 1º: '))
        n2 = float(input('Digite o novo valor do 2º: '))
        sleep(1)
print('FIM DO PROGRAMA')