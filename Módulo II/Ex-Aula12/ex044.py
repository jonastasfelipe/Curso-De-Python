# Elabore um programa que calcule o valor a ser pago por um 
# produto, considerando o seu preço normal e condição de pagamento:
# – à vista dinheiro/cheque: 10% de desconto
# – à vista no cartão: 5% de desconto
# – em até 2x no cartão: preço formal 
# – 3x ou mais no cartão: 20% de juros

#print('='*10,'LOJA JONATAS','='*10)
#valor = float(input('Preço das compras: R$'))
#print('''FORMAS DE PAGAMENTO
#[ 1 ] à vista dinheiro/cheque
#[ 2 ] à vista cartão
#[ 3 ] 2x no cartão
#[ 4 ] 3x ou mais no cartão''')
'''opção = int(input('Qual é a opção? '))
if opção == 1:
    print('Sua compra de R${:.2f} vai custar R${:.2f}'.format(valor, valor-valor*0.10))
elif opção == 2:
    print('Sua compra de R${:.2f} vai custar R${:.2f}'.format(valor, valor-valor*0.05))
elif opção == 3:
    print('Sua compra de R${:.2f} vai custar 2x de R${:.2f}'.format(valor, valor/2))
elif opção == 4:
    parcela = int(input('Quantas parcelas? '))
    print('Sua compra será parcelada em {}x de {:.2f} COM JUROS'.format(parcela, (valor+valor*0.20)/parcela))
    print('Sua compra dde R${:.2f} vai custar R${:.2f} no final.'.format(valor, valor+valor*0.20))
'''

# RESOLUÇÃO DO EXÉRCÍCIO
print('='*10,'LOJA JONATAS','='*10)
preço = float(input('Preço das compras: R$'))
print('''FORMAS DE PAGAMENTO
[ 1 ] à vista dinheiro/cheque
[ 2 ] à vista cartão
[ 3 ] 2x no cartão
[ 4 ] 3x ou mais no cartão''')
opção = int(input('Qual é a opção? '))
if opção == 1:
    total = preço - preço * 0.10
elif opção == 2:
    total = preço - preço * 0.05
elif opção == 3:
    total = preço 
    parcela = total / 2 
    print('Sua compra será parcelada em 2x de R${:.2f} SEM JUROS'.format(parcela))
elif opção == 4:
    total = preço + preço * 0.20
    totparc = int(input('Quantas parcelas? '))
    parcela = total / totparc
    print('Sua compra será parcelada em {}x de R${:.2f} COMM JUROS'.format(totparc, parcela))
else:
    total = preço
    print('OPÇÃO INVÁLIDA de pagamento. Tente novamente!')
print('Sua compra de R${:.2f} vai custar R${:.2f}'.format(preço, total))

