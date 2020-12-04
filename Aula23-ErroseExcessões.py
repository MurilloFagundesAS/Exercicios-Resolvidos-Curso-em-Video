
#  Erros sintaticos = quando foi escrito errado
#  Excessões = tratam-se de erros ocasionais ocorridos por motivos como tipo não aceito
try:  # Comando TENTE fazer isso
    a = int(input('Númerador: '))
    b = int(input('Denominador: '))
    r = a/b

#except:  # Exceto, se der erro faz isso
except Exception as erro:  # Diz: Exceto se der erro, e mostra qual erro foi
# Exception = excessão, usado para saber qual é, qual classe/tipo do erro
# um mesmo try pode ter vários except, cada um desses com seu tratamento, mas tem que colocar o tipo do erro
# except (ValueError, TypeError):
# except (ZeroDividionError):
# except (Keyboard Interrupt):  # não
    print(f'Deu ruim!!! Erro: {erro}')
# print(f'{erro.___cause__}')
# print(f'{erro.___class__}')
else:  # Opcional, realiza a ação se não deu erro
    print(f'O resultado de {a} / {b} = {r}')
finally:  # Opcional, executa independendo do resultado (com ou sem erro)
    print(f'Fim do Programa')
