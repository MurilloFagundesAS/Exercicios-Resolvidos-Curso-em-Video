n = int(input('Digite o número que você quer converter: '))
opcao = int(input('''
Digite:
[ 1 ] para converter para BINÁRIO
[ 2 ] para converter para OCTAL
[ 3 ] para converter para HEXADECIMAL\n'''))

if opcao == 1:
    print('{} conveertido em BINÁRIO é {}'.format(n, bin(n)))
elif opcao == 2:
    print('{} conveertido em OCTAL é {}'.format(n, oct(n)))
elif opcao == 3:
    print('{} conveertido em HEXADECIMAL é {}'.format(n, hex(n)))
else:
    print('Opção inválida!')