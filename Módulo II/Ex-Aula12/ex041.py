# A Confederação Nacional de Natação precisa de um programa que leia o ano de 
# nascimento de um atleta e mostre sua categoria, de acordo com a idade:
# - Até 9 anos: MIRIM
# - Até 14 anos: INFANTIL
# - Até 19 anos: JÚNIOR
# - Até 25 anos: SÊNIOR
# - Acima de 25 anos: MASTER

from datetime import date
atual = date.today().year
nasc = int(input('Ano de nascimento: '))
idade = atual - nasc
print('O aluno tem {} anos em {}, e a sua categoria é... '.format(idade, atual))
if idade <= 9:
    print('MIRIM')
elif 14 >= idade:
    print('INFANTIL')
elif 19 >= idade:
    print('JÚNIOR')
elif 25 >= idade:
    print('SÊNIOR')
else:
    print('MASTER')