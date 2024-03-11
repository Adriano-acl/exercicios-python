print('======= DESAFIO 07 AULA 07 =======')
#print('DESENVOLVA UM PROGRAMA QUE LEIA AS DUAS NOTAS DE UM ALUNO , CALCULE E MOSTRE A SUA MEDIA')
aluno = input('NOME ALUNO: ')
print('NOTA DO ALUNO {:*^10} '.format(aluno))
port = float(input('PORTUGUES : '))
mat = float(input('MATEMATICA : '))
med = (port + mat) /2
print('MEDIA = {}'.format(med))
