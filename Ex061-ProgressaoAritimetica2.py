primeiro = int(input('Digite o primeiro termo da PA: '))
razao = int(input('Digite a razão: '))

x = 10
pa = primeiro
while x != 0:
    print(f'{pa} ', end='')
    pa += razao
    x -=1