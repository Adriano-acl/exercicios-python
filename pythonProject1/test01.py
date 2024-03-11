print('PRATICA DE EXECICIO DA AULA 07')
nome = input('ESCREVA SEU NOME = ')
print('A SEGUIR VAMOS PEDIR PARA DIGITAR DOIS NÚMERO')
p = int(input('DIGITE O PRIMEIRO NÚMERO ? '))
s = int(input('DIGITE OUTRO NÚMERO ? '))
a = p + s
su = p - s
po = p ** s
d = p / s
print('A SOMA É = {} \nA SUBTRAÇÃO DOS DOIS É = {} \nA POTENCIA É = {} \nE A DIVISÃO = {}'.format(a,su,po,d))
print('OBRIGADO POR REALIZAR A ATIVIDADE {:*^20}'.format(nome))
