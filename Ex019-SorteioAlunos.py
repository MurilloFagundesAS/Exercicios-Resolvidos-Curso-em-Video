from random import randint

a = str(input('Digite o primeiro nome: '))
b = str(input('Digite o segundo nome: '))
c = str(input('Digite o terceiro nome: '))
d = str(input('Digite o quarto nome: '))

sorteio = randint(1,4)

if sorteio == 1:
    print('O sorteado foi: {}'.format(a))
elif sorteio == 2:
    print('O sorteado foi: {}'.format(b))
elif sorteio ==3:
    print('O sorteado foi: {}'.format(c))
else:
    print('O sorteado foi: {}'.format(d))

'''    
import random

a = str(input('Digite o primeiro nome: '))
b = str(input('Digite o segundo nome: '))
c = str(input('Digite o terceiro nome: '))
d = str(input('Digite o quarto nome: '))

alunos = [a,b,c,d]#criação de uma lista de itens

sorteio = random.choice(alunos) #função choice realiza escolhas
print('\nO aluno escolhido foi: {}'.format(sorteio))
'''