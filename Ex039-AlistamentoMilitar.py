#from datetime import date
#date.today().year
if ano == 2002:
    print('É ano de se alistar!')
elif ano < 2002:
    tempo = ano - 2002
    print('Já passou faz {} anos'.format(abs(tempo)))
else:
    tempo = 2020 - ano
    print('Ainda é cedo demais! Falta {} anos'.format(abs(tempo)))