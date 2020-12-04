from random import randint

player = int(input('De 0 a 5, qual número em que o Pc está pensando? '))
pc = randint(0,5)

while player != pc:
    print('Errou! O Pc pensou em {} e você disse {}'.format(pc, player))
    print('Vamos tentar de novo...')
    player = int(input('Qual é o número do PC, dessa vez? '))
    pc = randint(0,5)
print('Acertou! Você falou {} e o Pc falou {}'.format(player, pc))