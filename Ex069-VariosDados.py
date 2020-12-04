

maioridade = 0
homem = 0
mulher = 0
while True:
    print('{:=^36}'.format(' CADASTRO '))
    idade = int(input('Digite a IDADE da pessoa: '))
    sexo = str(input('Digite o SEXO da pessoa: [\33[31mF\33[m/\33[34mM\33[m] ')).strip().upper()

    if idade > 18:
        maioridade += 1

    if sexo == "M":
        homem += 1
    elif sexo == 'F':
        if idade < 20:
            mulher += 1
    else:
        print('OS dados informados não são aceitos!!!')
        break

    fim = str(input('Deseja registrar mais alguém? [S/N] ')).strip().upper()
    if fim == 'N':
        break
    print()
print(f'Você informou {maioridade} pessoa(s) maiores de 18 anos.')
print(f'Também informou também que tem {homem} homens.')
print(f'E informou, por fim, que há {mulher} mulheres menores de 20 anos')