# Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos Dólares ela pode comprar.

real = float(input('Quanto dinheiro vocẽ tem na carteira? R$ '))
dolar = real / 5.73
print('Com R${:.2f} você pode comprar US${:.2f}'.format(real, dolar))



