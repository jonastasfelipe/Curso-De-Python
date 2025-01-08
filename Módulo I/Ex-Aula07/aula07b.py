#Operadores e formatação de saída
n1 = int(input('Um valor: '))
n2 = int(input('Outro valor: '))
s = n1 + n2 #Soma
m = n1 * n2 #Multiplicação
d = n1 / n2 #Divisão
di = n1 // n2 #Divião Inteira
e = n1 ** n2 #Potenciação
print('A soma é {},\n o produto é {}\n e a divisão é {:.3f}.'.format(s,m,d), end=' ')
print('Divisão inteira {} e potênciação {}'.format(di,e))
# {:.3f} - Significa que depois do ponto ainda haverá 3 casas dedcimais e o "f" é de flutuante
# end=' ' - Continua na mesma linha do print
# \n - Quebra a linha 