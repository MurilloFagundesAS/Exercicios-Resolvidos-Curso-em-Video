from random import randint
from time import sleep

print('{:=^50}'.format(' Jogo do \33[31mPAR\33[m ou \33[34mIMPAR\33[m!!! '))

contagem = 0
while True:
    player = str(input('Você escolhe \33[31mPAR\33[m ou \33[34mIMPAR\33[m? ')).strip().upper()
    pc = 'm'
    playerMao = 0
    pcMao = 0
    soma = 0
    if player == 'PAR':
        pc = 'IMPAR'
        print(f'Você jogou \33[31m{player}\33[m !!!')
    elif player == 'IMPAR':
        pc = 'PAR'
        print(f'Você jogou \33[31m{player}\33[m !!!')
    else:
        print(f'Essa opção, \33[31m{player}\33[m, é inválida...\n')
        break
    playerMao = int(input('Quantos \33[31mDEDOS\33[m você vai jogar?\n(Lembrando que você só tem \33[31m5\33[m!) '))
    print(f'Você está jogando \33[31m{player}\33[m com \33[31m{playerMao}\33[m!')
    sleep(1)

    print('Eu... Digo, o \33[34mPC\33[m está jogando...')
    pcMao = randint(1,5)
    sleep(1)
    print(f'O \33[34mPC\33[m jogou \33[34m{pc}R\33[m com \33[34m{pcMao}\33[m dedos!')
    sleep(1)

    print('É AGORA!!!')
    soma = playerMao + pcMao
    sleep(1)
    print('O SSSSTOP...')
    sleep(1)
    print(f'O total de \33[31mDEDOS\33[m foi \33[34m{soma}\33[m!!!')

    if (soma % 2 == 0):
        if (player == 'PAR'):
            print(f'\33[31mVOCÊ\33[m GANHOU!!!'
                  f'\nTRAPAÇA, SÓ PODE!!'
                  f'\nEU... DIGO \33[34mPC\33[m NÃO QUER MAIS JOGAR!!!'
                  f'\nAFINAL, JÁ GANHEI, DIGO, O \33[34mPC\33[m'
                  f'\nJÁ GANHOU \33[34m{contagem}\33[m VEZES MESMO!!!')
            sleep(1)
            break
        elif (pc == 'PAR'):
            print('O \33[31mPC\33[m GANHOU!!!\nÉ POR QUE SOU MUITO BOM!!!\nDIGO... O \33[34mPC\33[m É BOM!!!')
            sleep(1)
            contagem +=1
        else:
            print('Ninguém ganhou...\nAmbos colocaram \33[31mPAR\33[m!!!')
            sleep(1)
    elif (soma%2 != 0):
        if (player == 'IMPAR'):
            print(f'\33[31mVOCÊ\33[m GANHOU!!!'
                  f'\nTRAPAÇA, SÓ PODE!!'
                  f'\nEU... DIGO \33[34mPC\33[m NÃO QUER MAIS JOGAR!!!'
                  f'\nAFINAL, JÁ GANHEI, DIGO, O \33[34mPC\33[m'
                  f'\nJÁ GANHOU \33[34m{contagem}\33[m VEZES MESMO!!!')
            sleep(1)
            break
        elif (pc == 'IMPAR'):
            print('O \33[31mPC\33[m GANHOU!!!\nÉ POR QUE SOU MUITO BOM!!!\nDIGO... O \33[34mPC\33[m É BOM!!!')
            sleep(1)
            contagem += 1
        else:
            print('Ninguém ganhou...\nAmbos colocaram \33[31mIMPAR\33[m!!!')
            sleep(1)

    print()
    print(f'Quero jogar de novo!\nDIGO... O \33[34mPC\33[m Quer!')
    sleep(1)

print(f'\33[31mJOGO\33[m \33[34mACABOU\33[m!!!')