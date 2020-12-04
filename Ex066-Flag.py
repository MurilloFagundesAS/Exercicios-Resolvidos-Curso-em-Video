n = 0
soma = 0
count = 0
while n != 999:
    n = int(input('Digite um número: '))
    if n == 999:
        break
    soma += n
    count += 1
print(f'Você digitou {count} números, cuja soma é {soma}!)