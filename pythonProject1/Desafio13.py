print('======= DESAFIO 13 AULA 07 =======')
print('FAÇA UM ALGORITIMO QUE LEIA O SALARIO DO FUNCIONARIO E MOSTRE O SEU NOVO SALARIO COM 15% DE AUMENTO')
fun = input('FUNCIONARIO : ')
sal = float(input('SALARIO DO FUNCIONARIO R$: '))
alm = sal * 0.15
almt = sal + (sal / 100) * 15
print('SALARIO DO FUNCIONARIO {} É DE R$: {}\nGANHOU UM AUMENTO DE 15%, SALARIO ATUAL R$:{:.2F} \nAUMENTO DE R$:{:.2F}'.format(fun,sal,almt,alm))
