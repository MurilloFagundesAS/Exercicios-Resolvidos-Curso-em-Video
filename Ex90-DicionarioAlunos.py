dicionario = {}
nome = str(input('Qual o nome do aluno? ')).strip()
media = float(input('Qual a média do aluno? '))
if media >= 7:
    situacao = 'APROVADO'
else:
    situacao = 'REPROVADO'

dicionario['Nome'] = nome
dicionario['Media'] = media
dicionario['Situação'] = situacao

for k, i in dicionario.items():
    print(f'{k} é {i}')