x = input('Digite algo: ')
print('Qual o tipo? ', type(x))
print('É númerico? ', x.isnumeric())
print('É alfabético? ', x.isalpha())
print('É alfanuerico?', x.isalnum())
print('Está tudo em maiuscula?', x.isupper())
print('Está tudo em minuscula?', x.islower())
print('É os dois?', x.istitle())