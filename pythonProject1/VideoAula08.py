import math
from math import sqrt, ceil, floor
num = int(input('DIGITE UM NUMERO: '))
raiz = math.sqrt(num)
print('NUMERO DIGITADO {} SUA RAIZ QUADRADA É {:.2f}'.format(num,raiz))
print('='*70)
print('outra forma de escrever o cod. format(num,math.ceil(raiz)\no numero digitado {} e sua raiz {}'.format(num,math.ceil(raiz)))
print('-'*70)
print('FORMA DE ESCREVER O COD. QUE ARREDONDE O A RAIZ P/ BAIXO\n o numero digitado é {} e a raiz dele é {}'.format(num,math.floor(raiz)))
print('*'*70)
