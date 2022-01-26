# Faça um programa que leia algo pelo teclado e mostre na tela o seu
# tipo primito e todas as informações possiveis sobre ela.

a = input('Digite algo:')
print('O tipo primitivo do valor {} é '.format(a), type(a))
print('{} Só tem espaços vazios?'.format(a), a.isspace())
print('{} É númerico'.format(a), a.isnumeric())
print('{} É alfabético?'.format(a), a.isalpha())
print('{} É alfanumérico?'.format(a), a.isalnum())
print('{} Está em maiúsculas?'.format(a), a.isupper())
print('{} Está em minúsculas?'.format(a), a.islower())
print('{} Está capitalizada?'.format(a), a.istitle())






