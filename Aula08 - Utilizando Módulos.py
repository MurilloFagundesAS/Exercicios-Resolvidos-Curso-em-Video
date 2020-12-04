# import math #adiciona a biblioteca/modulo inteiro
from math import sqrt, ceil #adiciona a função especifica da biblioteca/modulo
import emoji

n = int (input('Digite um número: '))

raiz = sqrt(n) #sqrt é raiz quadrada
print('a raiz de {} é {}'.format(n, ceil(raiz))) #ceil arredonda pra cima
                                                  #floor arredonda para baixo
print(emoji.emojize("É Isso ai :smile:", use_aliases=True))
