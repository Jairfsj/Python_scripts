# Escreva um programa que leia um valor em metros e o exiba convertido em centimetros a milímetros.

medida = float(input('Uma distância em metros: '))
cm = medida * 100
mm = medida * 1000
print('A media  de  {}m corresponde a {}cm e {}mm'.format(medida, cm, mm))


