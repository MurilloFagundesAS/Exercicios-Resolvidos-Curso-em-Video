casa = int(input('Qual o valor da casa que você deseja comprar? '))
salario = int(input('Qual o valor do seu salário? '))
anos = int(input('Em quantos anos você pretende pagar? '))

prestacao = casa/(anos*12)
print('Você pagaria R${:.2f} mensal'.format(prestacao))

if prestacao <= (salario * 0.30):
    print('Você pode financiar a casa!')
else:
    print('Você não pode financiar a casa!')