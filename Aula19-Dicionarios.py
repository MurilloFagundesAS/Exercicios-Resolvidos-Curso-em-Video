# Declaração
dicionario = dict()
dicionario = {'nome': 'José', 'idade': 22}

print(dicionario['nome'])
print(dicionario['idade'])

# Adicionar indices com suas variáveis
dicionario['sexo'] = 'M'
print(dicionario['sexo'])

# Remoção de elemento
del dicionario['idade']
print(dicionario)


filmes = {'titulo': 'Star Wars',
          'ano': '1977',
          'diretor': 'George Lucas'
        }
# Elementos como titulo, ano e diretor são chamados de chaves/keys
print(filmes.values())  # Values pega os valores, no caso Star Wars, 1977 e George Lucas
print(filmes.keys())  # Keys pega as chaves/keys, os indices (titulo, ano e diretor)
print(filmes.items())  # E Items pega tudo, tanto values quanto keys

for k, v in filmes.items():  #Parecido com enumerate(), dá os indices/keys e seus valores
    print(f'O {k} é {v}!')

'''
É possivel criar uma lista em que cada elemento/indice tem um dicionário
locadora = [{'titulo': '***', 'ano': '***', 'diretor': '***'},
            {'titulo': '***', 'ano': '***', 'diretor': '***'}},
            {'titulo': '***', 'ano': '***', 'diretor': '***'}}]
print(locadora[0]['titulo']) # mostraria o titulo do 'filme' no indice 0 da lista locadora
'''

print()
pessoas = {'nome':'José', 'idade': '22', 'sexo': 'masculino'}
print(pessoas)
print(pessoas['nome'])
print(f'O {pessoas["nome"]} tem {pessoas["idade"]} anos!')  # Usa aspas duplas para diferenciar
print(pessoas.values())
print(pessoas.keys())
print(pessoas.items())

for x in pessoas.keys():
    print(x)
for x in pessoas.values():
    print(x)
pessoas['nome'] = 'Maria'  # muda elemento
pessoas['peso'] = 100  # adiciona elemento
for x, y in pessoas.items():
    print(f'{x} = {y}')
print()


estado1 = {'nome': 'São Paulo', 'sigla': 'SP'}
estado2 = {'nome': 'Rio de Janeiro', 'sigla': 'RJ'}
brasil = []
print(estado1)
print(estado2)
brasil.append(estado1)
brasil.append(estado2)
print(brasil)
print(brasil[0])
print(brasil[0]['nome'])

pais = []
estado = {}
for i in range(0,3):
    estado['nome'] = str(input('Nome do Estado: ')).strip()
    estado['sigla'] = str(input('Sigla do Estado: ')).strip().upper()

    pais.append(estado.copy())  # Copia para não conectar as listas, [:] assim não funciona
print(pais)

for e in pais:  # for para a lista pais = [], para cada item e na lista pais[]
    for k, v in e.items():  # k é a chave/indice e o v é o valor
        print(f'O campo {k} contem o valor {v}!')
print()

for e in pais:
    for v in e.values():
        print(v)
