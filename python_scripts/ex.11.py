# Faça um algoritimo que leia o preço de um produto e mostre seu novo preço. com 5% de desconto.

preço = float(input('Qual é o preço do produto? R$: '))
novo = preço - (preço * 5 / 100)
print('Q produto que custava R$ {}, na promoção com desconto de 5% vai custar R$ {:.2f}'.format(preço, novo))


