dias = int(input("Quantos Dias Você Ficou Com o Carro? "))
km = float(input("Quantos quilometros você rodou? "))

total = (dias*60) + (km*0.15)
print("Você ficou {} dia(s) com o carro.\nAndou {}km.\nE o total que deve pagar é {}".format(dias, km, total))