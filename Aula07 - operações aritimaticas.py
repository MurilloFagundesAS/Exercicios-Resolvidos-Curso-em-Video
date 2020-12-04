a = int(input("Digite o Primeiro Número: "))
b = int(input("Digite o Segundo Número: "))
c = str(input('Digite algo: ')) # é possivel multiplicar string para repeti-la

soma = a+b
sub = a-b
mult = a*b
div = a/b
pot = a**b
pot2 = pow(a,b)     #forma diferente de fazer potência
divInt = a//b
restoDiv = a%b

print('{} + {} = {}'.format(a, b, soma))
print('{} - {} = {}'.format(a, b, sub))
print('{} * {} = {}'.format(a, b, mult))
print('{} / {} = {}'.format(a, b, div))
print('{} / {} = {:.3f}'.format(a, b, div)) # .3f significa 3 casas de float
print('{} ** {} = {}'.format(a, b, pot))
print('pow({}, {}) = {}'.format(a, b, pot2))
print('{} // {} = {}'.format(a, b, divInt))
print('{} % {} = {}'.format(a, b, restoDiv))
print()
print('{} '.format(c)*10) # é possivel repetir string
print('{:20} !!!'.format(c)) # é possivel aumentar o número de caracteres
print('{:>20} !!!'.format(c)) # com (> maior) é possivel alinhar a direita
print('{:=^20} !!!'.format(c)) # com o (circunfexo ^) é possivel centralizar com algum sinal



'''
Ordem de Precedencia:
1 - ()
2 - **
3 - /, //, *, % nesse caso, quem aparecer primeiro na equação é resolvido primeiro
4 - + 2 -


\n pra quebrar linha e end='' vazio pra não quebrar, se tiver um simbolo ele esvreve
e segue a vida dele
'''