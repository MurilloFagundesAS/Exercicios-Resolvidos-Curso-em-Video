n = int(input('Digite quantos termos da Sequência de Fibonacci você deseja ver: '))

x = 0
a = 0
b = 1
print(f'{a} {b} ', end='')
while x != n+1:
    soma = a + b
    print(f'{soma} ', end='')
    a = b
    b = soma
    x += 1