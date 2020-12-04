km = int(input('A quantos km/h você está? '))

if km > 80:
    print('\nVocê foi multado!!!')

    multa = (km - 80) * 7
    print('Sua multa é de R${:.2f}'.format(multa))
else:
    print('\nEssa foi por pouco...')