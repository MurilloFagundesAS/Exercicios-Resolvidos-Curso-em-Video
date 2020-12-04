saque = int(input('Quanto você quer SACAR? '))
x = saque
nota50 = 0
nota20 = 0
nota5 = 0
moeda1 = 0

while True:
    if saque >= 50:
        saque -=50
        nota50 += 1
    elif (saque < 50) and (saque >= 20):
        saque -= 20
        nota20 += 1
    elif (saque < 20) and (saque >= 5):
        saque -= 5
        nota5 += 1
    elif saque < 5:
        saque -=1
        moeda1 +=1

    if saque == 0:
        break

print(f'O Saque de \33[31mR${x:.2f}\33[m será em:')
if nota50>0:
    print(f' \33[31m{nota50}\33[m notas de \33[31mR$R$50,00\33[m')
if nota20>0:
    print(f' \33[31m{nota20}\33[m notas de \33[31mR$R$20,00\33[m')
if nota5>0:
    print(f' \33[31m{nota5}\33[m notas de \33[31mR$R$5,00\33[m')
if moeda1>0:
    print(f' \33[31m{moeda1}\33[m moedas de \33[31mR$R$1,00\33[m')