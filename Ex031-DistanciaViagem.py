km = int(input('Quantos km você pretende viajar? '))

if km <= 200:
    preco = km * 0.50
    print('Sua passagem custará R${:.2f}'.format(preco))
else:
    preco = km * 0.45
    print('Sua passagem custará R${:.2f}'.format(preco))