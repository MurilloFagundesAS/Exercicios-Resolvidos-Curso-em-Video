#from datetime import date
#date.today().year

nome = str(input('Qual o seu nome? ')).strip()
ano = int(input('Em que ano você nasceu? '))

idade = 2020 - ano

if idade <= 9:
    print('Olá {}. Você tem {} anos. E sua categoria é: MIRIM'.format(nome, abs(idade)))
elif (idade > 9) and (idade <= 14):
    print('Olá {}. Você tem {} anos. E sua categoria é: INFANTIL'.format(nome, abs(idade)))
elif (idade > 14) and (idade <= 19):
    print('Olá {}. Você tem {} anos. E sua caregoria é: JUNIOR'.format(nome, abs(idade)))
elif (idade > 19) and (idade <= 20):
    print('Olá {}. Você tem {} anos. E sua caregoria é: SÊNIOR'.format(nome, abs(idade)))
else:
    print('Olá {}. Você tem {} anos. E sua caregoria é: MASTER'.format(nome, abs(idade)))