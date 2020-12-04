soma = 0
for i in range(1,501):
    if i % 2 != 0 and i % 3 == 0:
        soma = soma + i
print('Total: \33[31m{}\33[m'.format(soma))