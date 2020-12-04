frase = 'Curso em Video Python'#aspas simples

#fatiamento
frase = [9] #pega a letra na posição 9 do indice, lembrando que começa a contar do 0
frase[9:13] #pega do 1º ao penultimo, excluindo o último
frase[9:21:2]#passo 2
frase[:5] #pega do zero ao 5, igual a [0:5]
frase[16:] #pega do 16 até o final, igual a [16:x]
frase[9::3] #pega do 9 até o final, a passo 3

#analise
len(frase) #mostra o comprimento, quantidade de números de caracteres
frase.count("o")# conta a quantidade de caracteres dentro das aspas
frase.count("o", 0,13)#conta do 0 ao 13, exluindo-o, e procura o que está em aspas
frase.find("deo")#procura e mostra aonde começou
frase.find("Android")#se não haver o que ele está procurando, ele retorna -1
in frase "curso"#indica se existe o que está entre parenteses,

#transformação
frase.replace("Python", "Androide")#troca o primeiro pelo segundo
frase.upper()#troca td pra maiusculas
frase.lower()#troca tudo por minuscula
frase.capitalize()#só a primeira fica em maiuscula
frase.title()#encontra palavras,as diferenciando com o espaço, e deixa a primeira letra maiuscula

frase = '   Aprenda a Python   '
frase.strip()#tira os espaços excedentes com começo e do final
frase.rstrip()#r de right/direita, só remove os últimos, a direita da string
frase.lstrip()#l de left/esquerda, só remove os primeiros, a esquerda da string

#divisão
frase.split()#divide onde tem espaços na string, formando várias strings,
#faz uma lista com palavras da string, cada elemento tem um número, a partir do 0

#junção
"-".join(frase)# junta com as strings colocando entre elas o que está entre aspas

#outros
print("""
Caralho
que
fodá!!!
""")
