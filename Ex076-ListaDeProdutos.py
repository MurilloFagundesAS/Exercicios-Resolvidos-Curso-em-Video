produtos = ('Pão', 0.50, 'Leite', 4, 'Requeijão', 5, 'Nescau', 6.50, 'Frios', 3.50)

print('-'*40)
print('{:^40}'.format('SUPERMERCADO'))
print('-'*40)

'''for item in range(0, 10, 2):
    preco = item+1
    print('{} {:.>20} {}'.format(produtos[item], 'R$', produtos[preco]))
print('-'*35)'''

for item in range(0,len(produtos)):
    if item % 2 == 0:
        print(f'{produtos[item]:.<30}', end='')
    else:
        print(f' R${produtos[item]:.2f}')
print('-'*40)