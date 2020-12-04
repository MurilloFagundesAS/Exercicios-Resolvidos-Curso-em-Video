'''
variavel = ''

tupla = ()  # Tuplas são imutáveis
tupla = '', '', ''

lista = []

dicionário = {}
'''

lanche = ('hambuguer', 'batatinha', 'refri', 'sorvetinho')
print(lanche)
print(lanche[1])
print(lanche[-1])  # O zero é o primeiro direita pra esquerda
print(lanche[0:2])  # Vai do 0 ao 2 desconsiderando o último
print(lanche[0:])  # Vai do zero em diante, até o final
print(lanche[:3])  # Vai do zero em diante, desconsiderando o último
print(len(lanche))  # O len serve pra contar itens dentro da tupla
print(sorted(lanche))  # O sorted organiza alfabeticamente e/ou em ordem númerica
print(lanche[1],",", lanche[2],"\n")

for comida in lanche:
    print(f'Vou comer {comida}')  # Tem efeito similar a print{f'{lanche[i]}'}
print()

for food in range(0, len(lanche)):
    print(lanche[food])
print()

for posicao, alimento in enumerate(lanche):  # O enumerate dá a posição e o item
    print(f'Vou comer {posicao} {alimento}')

a = (1,2,3)  # Tuplas também servem de Conjuntos
b = (3,4,5)
c = a + b
print(a)
print(b)
print(c)
print(c.count(3))  # O Count conta quantas vezes aparece tal elemento
print(c.index(1))  # O index mostra o indice/posição de tal elemento
print(c.index(3, 3))  # Index a partir da posição 3
print()

pessoa = ('Marcos', 'Tabata', 'Umberto', 'Paulo', 'Denise', 'Vitor Tarcisio', 'Comandante')
print(f'{pessoa}')

del(pessoa)  # Del deleta toda a tupla, sendo impossivel apagar um elemento