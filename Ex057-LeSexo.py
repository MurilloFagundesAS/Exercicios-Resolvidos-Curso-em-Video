sexo = 'F'

while sexo == 'M' or sexo == 'F':
    sexo = str(input('Digite o sexo da pessoa: [M/F] ')).strip().upper()
while sexo != 'M' and sexo != 'F':
    print('Você digitou um valor inválido!')
    sexo = str(input('Digite novamente o sexo da pessoa: [M/F] ')).strip().upper()