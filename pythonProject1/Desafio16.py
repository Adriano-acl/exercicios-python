import math
from math import floor
print('======= DESAFIO 16 AULA 08 =======')
print('CRIE UM PROGRAMA QUE LEIA UM NUMERO REAL QUALQUER PELO TECLADO \nE MOSRE NA TELA A SUA PORÇÃO INTEIRA')
print('-'*70)
num = float(input('DIGITE UM NÚMERO : '))
u = math.floor(num)
print('O NÚMERO DIGITADO É {} E SUA PARTE INTEIRA É {}'.format(num,u))
