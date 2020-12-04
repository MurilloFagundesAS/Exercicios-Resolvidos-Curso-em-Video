while True:
    n = int(input('Qual tabuada você quer saber? '))
    if n < 0:
        break
    x = 1
    tabuada = 0
    while x <= 10:
        tabuada = x * n
        print(f'{n} X {x} = {tabuada}')
        x += 1
print(f'Você digitou {n}!')
