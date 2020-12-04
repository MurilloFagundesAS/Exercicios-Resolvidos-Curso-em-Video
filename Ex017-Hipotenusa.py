from math import sqrt, hypot

catetoA = float(input('Digite o valor do Cateto Adjacente: '))
catetoO = float(input('Digite o valor do Cateto Oposto: '))

hipotenusa = sqrt((catetoA**2) + (catetoO**2))

hipotenusa2 = hypot(catetoO, catetoA)

print('\nCateto Adjacente = {:.2f}\nCateto Oposto = {:.2f}\nHipotenusa = {:.2f}, Hipotenusa 2 = {}'.format(catetoA, catetoO, hipotenusa, hipotenusa2))