#print('======= DESAFIO 12 AULA 07 =======')
#print('FAÇA UM ALGORITIMO QUE LEIA O PREÇO DE UM PRODUTO E MOSTRE O SEU NOVO PREÇO COM 5% DE DESCONTO')
p = input('PRODUTO A VENDA : ')
v = float(input('PREÇO DO PRODUTO : R$ '))
t = v * 0.05
s = v - (v / 100) * 5
x = v - (v * 5 / 100)
print('PRODUTO A VENDA {} COM O VALOR DE R$ {}\nA VISTA COM DESCONTO DE 5% R$ {}\nTOTAL DE DESCONTO {:.2f}'.format(p,v,s,t))
#print('outra fomar de %  {}'.format(x))
