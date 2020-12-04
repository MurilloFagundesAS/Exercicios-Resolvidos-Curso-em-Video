frase = str(input('Digite uma frase: ')).strip().upper()

div = frase.split()
juntar = "".join(div)
print(juntar)

x = len(juntar)
y = juntar.find(juntar[x:0:-1])
print(juntar[x:0:-1])

if y == 0:
    print('É PALINDROMO')
else:
    print('NÃO É PALINDROMO')
