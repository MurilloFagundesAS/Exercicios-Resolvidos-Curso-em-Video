def mostrarLinha():  # definir função
    print('1')  # É possível apertar as setas para omitir a função no código

# 2 linhas para não reclamar
mostrarLinha() # exemplo de uso
mostrarLinha()
mostrarLinha()

def texto(msg):  # função com parametro: caso em que está entre () é preenchido e pode ser alterado
    print('X'*30)
    print(msg)
    print('X'*30)

texto('olá')


def soma(a, b): #exemplo de 2 parametros
    print(f'A = {a} e B = {b}')
    s = a + b
    print(f'A soma é igual a {s}')


soma(1, 2)  # Só é possivel colocar a quantidade de parametros, nesse caso, 2
soma(b=1, a=2)  # É possivel deixar explicitar qual parametro recebe qual valor/entrada


def contador(*num):  # O * indica desempacotar, serve pra entrar com quantidade desconhecida de valores
    tantos = len(num) # *num funciona como uma tupla
    print(f'Recebi os valores {num} e foram {tantos} números')


contador(0, 1)
contador(1, 2, 3)
contador(1, 2, 4)

# também é possivel criar função com listas, mas não é desempacotar
def dobra(lista):  #Pode colocar qualquer nome
    pos = 0
    while pos < len(lista):
        lista[pos] *= 2
        pos += 1

valores = [1, 2, 3, 4]
print(valores)
dobra(valores)
print(valores)