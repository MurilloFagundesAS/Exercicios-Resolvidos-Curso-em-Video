cidade = str(input("Qual o nome de sua cidade? "))
# print(cidade[:5].upper == 'SANTO')
div = cidade.split()

if div[0] == 'Santo':
    print('Começa com Santo!')
else:
    print('Não começa...')