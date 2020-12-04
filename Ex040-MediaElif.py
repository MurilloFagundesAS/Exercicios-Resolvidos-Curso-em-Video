x1 = float(input('Qual sua primeira nota? '))
x2 = float(input('Qual sua segunda nota? '))

media = (x1+x2)/2

if media < 5.0:
    print("REPROVADO!")
elif (media >= 5.0) and (media <= 6.9):
    print('RECUPERAÇÃO!')
else:
    print('APROVADO!')