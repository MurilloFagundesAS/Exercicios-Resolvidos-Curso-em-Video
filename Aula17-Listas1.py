lista = [1,2,3]
# lista vazia : lista = [] ou lista = list()
print(lista)

i = 1
lista2 = []
while i <= len(lista):
    lista2.append(lista.index(i))
    lista2.append(lista[i])
    i+=1
print(lista2)


# lista.append('append')  # Adiciona no final da lista
# # print(lista)
# #
# # lista.insert(1,'insert')  # Adiciona entre os elementos da lista
# # print(lista)
# #
# # # Todos os casos reposicionam o indice da lista
# # del lista[3]  # Deleta
# # print(lista)
# #
# # lista.pop(3)  # Deleta, usado normalmente para eliminar o último elemento
# # print(lista)
# # lista.pop()
# # print(lista)
# #
# # lista.remove(1)  # Deleta o elemento indicado, mas só a primeira ocorrência
# # print(lista)
# #
# # # list é função pra declarar lista
# # lista = list(range(1,11))
# # print(lista)
# #
# # lista.sort(reverse=True)  # parametro reverse inverte
# # print(lista)
# #
# # lista.sort()  # sort organiza a lista por ordem alfabetica/númerica crescente
# # print(lista)
# #
# # print(len(lista))  # a função len dá a quantidade de itens numa lista
# #
# # for posicao, valor in enumerate(lista):  # enumerate dá o indice e o elemento da lista
# #     print(f'Na posição {posicao} encontra-se o valor {valor}!')
# #
# # for num in range(0,4):
# #     lista.append(int(input('Digite um valor: ')))
# # print(lista)
#
#
# listaB = lista  # no Python, listas estão interligadas se forem igualadas
# print(listaB)
#
# listaC = lista[:] # no Python, nesse caso, só copiei a lista e seus elementos
# listaC[7] = 1010
# print(listaC)
