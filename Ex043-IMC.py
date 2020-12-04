peso = float(input('Qual seu peso? '))
altura = float(input('Qual sua altura? '))

imc = peso/(altura**2)

if imc < 18.5:
    print('IMC = {:.1f}. Você está ABAIXO DO PESO!'.format(imc))
elif (imc >= 18.5) and (imc < 25):
    print('IMC = {:.1f}. Você está no PESO IDEIAL!'.format(imc))
elif (imc >= 25) and (imc < 30):
    print('IMC = {:.1f}. Você está com SOBREPESO!'.format(imc))
elif (imc >= 30) and (imc < 40):
    print('IMC = {:.1f}. Você está com OBESIDADE!'.format(imc))
else:
    print('IMC = {:.1f}. Você está com OBESIDADE MÓRBIDA'.format(imc))