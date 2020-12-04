#help(print)
#print(input.__doc__)

# váriavel global é acessível a todos, local só a determinada parte (exemplo, uma função)
def exemplo(v1 = 0, v2=0, v3=0): # Nesse caso, as variaveis valem 0 se não colocar nada nelas
    s = v1 + v2 + v3
    print(f'A soma vale {s}')
    a = 0
    print(f'a local = {a}')
    #global a  # global = usado para definir a variável como global no código
    print(f'agora, a local = {a}')
    return s

a = 9
print(f'a global = {a}')
#exemplo(1,2,3)
#variavel = exemplo(1,2,3)  # Nesse caso, ela devolve a resposta para a variável
print(f'O retorno = {exemplo(1,2,3)}')
