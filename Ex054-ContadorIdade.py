from datetime import date

menores = 0
maiores = 0
for i in range(1,8):
    ano = int(input('Em que ano a pessoa nasceu? '))
    idade = date.today().year - ano
    if idade < 21:
        menores += 1
    else:
        maiores += 1
print('{} ainda são MENORES\nE {} já são MAIORES'.format(menores, maiores))
