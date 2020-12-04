from time import sleep

def maior(*num):
        print('Analisando os valores....')
        sleep(1)
        if len(num) == 0:
            print(f'Não foram informados nenhum valor...')
        else:
            print(f'Os Valores são: {num}')
            print(f'Foram informados {len(num)} números, cujo maior é {max(num)}')

maior(1, 2, 4, 5, 3, 2)
maior(1, 14)
maior(-1, -10, -7)
maior()
