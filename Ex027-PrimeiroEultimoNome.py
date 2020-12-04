
nome = str(input('Digite seu nome: ')).strip()

div = nome.split()

print('Seu primeiro nome é {}'.format(div[0]))
print('Seu último nome é {}'.format(div[len(div)-1]))#len conta quantos tem em div
#e depois tira -1 da contagem