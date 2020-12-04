l = float(input('Qual a Largura da Parede? '))
h = float(input('Qual a Altura da Parede? '))

area = l * h
pintar = area//2

print()
print('Largura = {:.2f}\nAltura = {:.2f}\nArea da Parede = {:.2f}m2\nE preciso de {}l de tinta para pintar'.format(l, h, area, pintar))