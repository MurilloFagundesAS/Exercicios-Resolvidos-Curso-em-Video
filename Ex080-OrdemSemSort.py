lista = []

for i in range(0, 5):
    x = int(input('Digite um número: '))
    if i == 0:
        lista.append(x)
        print('Adicionado o primeiro número da lista!')
    else:
        if x > max(lista):
            lista.append(x)
            print('Adicionado ao final da lista!')
        elif x < min(lista):
            lista.insert(0, x)
            print('Adicionado no inicio da lista!')
        else:
            for j in range(0, len(lista)):
                if lista[j] < x < lista[j+1]:
                    print(f'Adicionado entre {lista[j]} e {lista[j + 1]}!')
                    lista.insert(lista.index(lista[j+1]), x)
print(lista)