frase = str(input('Escreva uma frase: ')).strip().upper()

print('A letra "A" aparece {} vezes'.format(frase.count('A'))
print('A primeira letra "A" está na posição {}'.format(frase.find('A')))
print('A primeira letra "A" está na posição {}'.format(frase.rfind('A'))) # find a partir de right