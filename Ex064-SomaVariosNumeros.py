n = 0
soma = 0
contagem = 0
while n!= 999:
    n = int(input('Digite um número: '))
    if n != 999:
        soma += n
        contagem += 1
print(f'Você dititou {contagem} numeros e a soma de todos eles é {soma}!')