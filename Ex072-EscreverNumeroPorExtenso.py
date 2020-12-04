num = ('Zero', 'Um', 'Dois', 'Três', 'Quatro', 'Cinco', 'Seis', 'Sete', 'Oito', 'Nove', 'Dez',
       'Onze', 'Doze', 'Treze', 'Quatorze', 'Quinze', 'Dezesseis', 'Dezessete', 'Dezoito',
       'Dezenove', 'Vinte')

x = int(input('Digite um número de 0 a 20: '))
while True:
    if (x >= 0) and (x <= 20):
        print(f'Você digitou \33[31m{num[x]}\33[m')
        break
    else:
        x = int(input(f'Numero inválido. Tente de Novo: '))