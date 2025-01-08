#Faça um algoritimo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento.
n = float(input('Seu salário: '))
p = n*0.15
s = n+p
print('Seu salário era R$ {:.2f}, agora com um aumento de 15%, seu salário é R$ {:.2f}'.format(n,s))
print('Um aumento de R$ {:.2f}'.format(p))