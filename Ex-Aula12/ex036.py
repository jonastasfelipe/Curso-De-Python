# Escreva um programa para aprovar o empréstimo bancário para a 
# compra de uma casa. Pergunte o valor da casa, o salário do 
# comprador e em quantos anos ele vai pagar. A prestação mensal 
# não pode exceder 30% do salário ou então o empréstimo será negado.

'''valor = float(input('Qual o valor da casa? '))
salário = float(input('Qual o seu salário? '))
anos = float(input('Quanto anos irá pagar? '))
if valor/(anos*12) < salário*0.30:
    print('Parabéns! Seu imprestimo foi aprovado')
else:
    print('Desculpa. Seu emprestimo foi recusado')
print('O valor total a se pagar é de R${}, parcelado em {:.} mêses de R${}.'.format(valor, anos*12, 120/(anos*12)))
'''

# Resolução do exercício
casa = float(input('Valor da casa: R$ '))
salário = float(input('Salário do comprador: R$ '))
anos = int(input('Quantos anos de financiamento? '))
prestação = casa / (anos * 12)
mínimo = salário * 0.30
print('Para pagar uma casa de R${:.2f} em {} anos, a prestação será de R${:.2f}'. format(casa, anos, prestação))
if prestação <= mínimo:
    print('Empréstimo pode ser CONCEDIDO!')
else:
    print('Empréstimo NEGADO!')
