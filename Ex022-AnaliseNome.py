nome = str(input('Qual o seu nome? ')).strip()# tira espaço antes e depois

print('seu nome em maiscula é: ', nome.upper())
print('Seu nome em minusculo é: ', nome.lower())

div = nome.split()
juntar = ''.join(div)
print('Seu nome tem',len(juntar), 'letras')
# print(''.format(len(nome) - nome.count' ')) # tira os espaços quando for contar letras
print('E seu primeiro nome tem', len(div[0]) , 'letras')