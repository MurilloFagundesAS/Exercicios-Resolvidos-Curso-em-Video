from random import randint
n = int(input("Tente adivinhar que número, entre 0 e 5, estou pensando? "))

pc = randint(0,5)

if n == pc:
    print('Acerto Miseravi!!!')
else:
    print('Errouuuuuu!!!')

print('Você chutou {} e eu pensei em {}'.format(n,pc))