import math

ang = float(input('Digite o ângulo? '))

angRad = math.radians(ang)#função para transformar um valor em radianos

seno = math.sin(angRad) #essas funções dão resultado em Radianos, devendo ser transfromadas
cose = math.cos(angRad)
tang = math.tan(angRad)

print('\nÂngulo = {:.0f}\nSeno = {:.2f}\nCoseno = {:.2f}\nTangente = {:.2f}'.format(ang, seno, cose, tang))