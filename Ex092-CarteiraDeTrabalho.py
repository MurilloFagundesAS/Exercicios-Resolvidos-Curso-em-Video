from datetime import date
dicionario = {}

nome = str(input('Nome: ')).strip()
dicionario['nome'] = nome
ano = int(input('Ano de Nascimento: '))
idade = date.today().year - ano
dicionario['idade'] = idade
carteira = int(input('Carteira de Trabalho: [Digite 0 se não tiver] '))
if carteira != 0:
    dicionario['ctps'] = carteira
    contratacao = int(input('Ano de contratação: '))
    dicionario['contratação'] = contratacao
    aposenta = abs((date.today().year - contratacao) - 35) + idade
    dicionario['aposentadoria'] = aposenta
    salario = float(input('Salário: '))
    dicionario['salário'] = salario
else:
    dicionario['ctps'] = 'Não tem'
print(dicionario)

for k, v in dicionario.items():
    print(f'{k} = {v}')
