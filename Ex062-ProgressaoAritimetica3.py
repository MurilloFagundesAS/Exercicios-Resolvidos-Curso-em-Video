primeiro = int(input('Digite o primeiro termo da PA: '))
razao = int(input('Digite a razão: '))

x = 10
pa = primeiro
fim = 1
while fim > 0:
    while x != 0:
        print(f'{pa} ', end='')
        pa += razao
        x -=1
    continuar = int(input('\nDeseja mostrar mais quantos termos? (Se nenhum digite 0) '))
    if continuar != 0:
        x = 10 + continuar
    else:
        fim = -100
    pa = primeiro