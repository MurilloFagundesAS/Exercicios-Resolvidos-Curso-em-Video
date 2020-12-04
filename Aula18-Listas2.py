# Lista composta
pessoas = [['José', '22'], ['Maria', '55']]
print(pessoas[1])
print(pessoas[0][0])

teste = []
print(teste)
teste.append('Gustavo')
teste.append(40)
#teste.append([variavel1, variavel2, etc])
#teste[indice].append()  # Adiciona no indice
print(teste)
galera = list()
galera.append(teste[:])  # Também iguala equações, deixando-as conectadas

teste[0] = 'Mariana'  # A coneção é evitada fazendo copia
teste[1] = 22
galera.append(teste[:])  # Assim copia
print(galera)

for pessoa in galera:
    print(pessoa)
    print(pessoa[0])

grupo = list()
individuo = list()

for dado in range(0,3):
    individuo.append(str(input('Qual o Nome? ')))
    individuo.append(int(input('Qual a Idade? ')))
    print(individuo)

    grupo.append(individuo[:])  # Copia pra n ligar das listas e apagar ambas
    individuo.clear()
print(grupo)

for ser in grupo:
    if ser[1] >= 21:
        print(ser)
