# Crie um programa que leia duas notas de um aluno e calcule sua 
# média, mostrando uma mensagem no final, de acordo com a média 
# atingida:
# - Média abaixo de 5.0: REPROVADO
# - Média entre 5.0 e 6.9: RECUPERAÇÃO
# - Média 7.0 ou superior: APROVADO

n1 = float(input('Primeira nota: '))
n2 = float(input('Segunda nota: '))
média = (n1 + n2) / 2
if média < 5:
    print('Sua média é de: {} pontos'.format(média))
    print('REPROVADO')
elif 7 > média >= 5:
    print('Sua média é de: {} pontos'.format(média))
    print('RECUPERAÇÂO')
else:
    print('Sua média é de: {} pontos'.format(média))
    print('APROVADO')
    