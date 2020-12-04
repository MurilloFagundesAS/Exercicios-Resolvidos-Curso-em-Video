frase = 'Curso em Video Python'

print(frase)
print()

print(frase[3])
print(frase[4:13])
print(frase[:21])
print(frase[0:10:2])
print(frase[::2])

print("""
Test
And
Do!!!
""")

print(frase.count('o'))
print(frase.upper().count('O'))
print(len(frase))

print(frase.replace('Python', 'Android'))

frase = frase.replace('Python', 'Curso do Gustavo Guanabara')
print(frase)

print('Curso do Gustavo Guanabara' in frase)
print(frase.find('Curso do Gustavo Guanabara'))

print(frase.split())

div = frase.split()
print(div[6][1]) #o primeiro [] é indice e o segundo posição de caracter daquele indice