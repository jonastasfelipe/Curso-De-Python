# Escreva um programa que pergunte o salário de um funcionário e calcule o 
# valor do seu aumento. Para salários superiores a R$1250,00, 
# calcule um aumento de 10%. Para os inferiores ou iguais, 
# o aumento é de 15%.

salário = float(input('Qual o valor do seu salário? R$'))
if salário > 1250:
    aumento = salário + (salário*0.10)
else:
    aumento = salário + (salário*0.15)
print('O valor do seu salário era R${:.2f}, agora é de R${:.2f}'.format(salário, aumento))