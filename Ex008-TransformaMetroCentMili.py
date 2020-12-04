a = float(input("Digite o valor em metros: "))

cent = a*100
mili = a*1000

print('{:.2f}m em centimetros é {:.2f}cm\ne em minimetros {:.2f}mm'.format(a, cent, mili))