p1 = float(input('Digite o peso da 1ª pessoa: '))
p2 = float(input('Digite o peso da 2ª pessoa: '))
p3 = float(input('Digite o peso da 3ª pessoa: '))
p4 = float(input('Digite o peso da 4ª pessoa: '))
p5 = float(input('Digite o peso da 5ª pessoa: '))
maior : float
menor : float

if (p1>p2) and (p1>p3) and (p1>p4) and (p1>p5):
    maior = p1
elif (p2>p1) and (p2>p3) and (p2>p4) and (p2>p5):
    maior = p2
elif (p3>p1) and (p3>p2) and (p3>p4) and (p3>p5):
    maior = p3
elif (p4>p1) and (p4>p2) and (p4>p3) and (p4>p5):
    maior = p4
elif (p5>p1) and (p5>p2) and (p4>p3) and (p5>p4):
    maior = p5

if (p1<p2) and (p1<p3) and (p1<p4) and (p1<p5):
    menor = p1
elif (p2<p1) and (p2<p3) and (p2<p4) and (p2<p5):
    menor = p2
elif (p3<p1) and (p3<p2) and (p3<p4) and (p3<p5):
    menor = p3
elif (p4<p1) and (p4<p2) and (p4<p3) and (p4<p5):
    menor = p4
elif (p5<p1) and (p5<p2) and (p4<p3) and (p5<p4):
    menor = p5

print('O menor peso é {:.2f}kg\nE o maior peso {:.2f}kg'.format(menor, maior))