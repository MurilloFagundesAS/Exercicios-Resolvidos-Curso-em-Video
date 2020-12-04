def contador(inicio, fim, passo):
    print(f'Contagem de {inicio} até {fim} de {passo} em {passo}')
    if passo == 0:
        passo = 1
    if inicio < fim:
        while inicio <= fim:
            print(f'{inicio} ', end='')
            inicio += passo
    elif inicio > fim or passo < 0:
        while inicio >= fim:
            print(f'{inicio} ', end='')
            inicio -= abs(passo)
    print()


contador(1, 10, 1)
contador(10, 1, 2)

inicio = int(input('Digite o começo: '))
fim = int(input('Digite o final: '))
passo = int(input('Digite o passo: '))
contador(inicio, fim, passo)
