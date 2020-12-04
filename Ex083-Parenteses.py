lista = []
exp = str(input('Digite uma Expressão: '))
parenteses1 = 0
parenteses2 = 0

for simb in exp:
    if simb == '(':
        parenteses1 += 1
    elif simb == ')':
        parenteses2 +=1

if parenteses1 == parenteses2:
    print('A expressão é válida!')
else:
    print('A expressão é inválida')
'''
lista = []
x = str(input('Digite uma expressão: ')).strip().lower()

parenteses1 = x.count('(')
parenteses2 = x.count(')')

print(f'Essa expresão tem {parenteses1} parenteses abertos')
print(f'Essa expresão tem {parenteses2} parenteses fechados')
if parenteses1 == parenteses2:
    print('Essa expressão é válida!')
else:
    print('Essa expressão não é valida!')'''