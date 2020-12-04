print('\33[4;30;43mMurillo\33[m José')


'''
print('\33[7;30;40m José')# formata TD, estilo da fonte, cor da letra e a cor do fundo
print('\33[30;42m José') #formatação de letra padrão com cor e fundo
print('\33[m José') #faz fundo preto e letra branca (padrão)
print('\33[7;30m José') #faz fundo branco e letra preta


                        PADRÃO ANSE
# \33[ estilo da fonte; cor do texto; cor de fundo m
para estilo:
0 = nada
1 = negrito
3 = italico
4 = sublindado
7 = negativo (inverte cor)

para cor de texto: (tudo começa com 3)      para fundo (tudo começa 4)
30 - branco                                 40 - branco
31 - vermelho                               41 - vermelho
32 - verde                                  42 - verde
33 - amarelo                                43 - amarelo
34 - azul                                   44 - azul
35 - magenta                                45 - magenta
35 - ciano                                  45 - ciano
36 - cinza                                  46 - cinza
'''