primeiro = int(input('Qual é o primeiro termo? '))
razao = int(input('Qual é a razão? '))

for i in range(1, 11):
    print('{} '.format(primeiro), end="")
    primeiro = primeiro + razao

'''
primeiro = int(input('')
razao = int(input('')
decimo = primeiro + (10-1) * razao
for i in range (primeiro, decimo, razao):
    print (i)
'''