n = int(input('Digite um número para saber seu fatorial: '))

x = 1
fatorial = 1
while x != n+1:
    fatorial = fatorial * x
    x += 1
print(f'O fatorial de {n} é igual a {fatorial}')