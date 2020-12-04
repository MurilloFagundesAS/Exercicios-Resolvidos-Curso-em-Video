nome = str(input("Qual o Seu nome? "))

teste = nome.find('Silva')

if teste != -1:
    print('Você tem Silva no nome!')
else:
    print('Você não tem Silva no nome!')

#print('Você tem Silva no nome? '.format('SILVA' in nome.upper))