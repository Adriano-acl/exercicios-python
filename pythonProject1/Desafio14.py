print('======= AULA 07 DESAFIO 14 =======')
print('ESCREVA UM PROGRAMA QUE CONVERTA UMA TEMPERATURA DIGITADA EM ºC E CONVERTA EM ºF.')
c = float(input('TEMPERATURA ºC = '))
f = (c * 1.8) + 32
print('TEMPERATURA ºF = {}'.format(f))
fa = float(input('TEMPERATURA ºF = '))
ce = (fa - 32) / 1.8
print('TEMPERATURA ºC = {}'.format(ce))