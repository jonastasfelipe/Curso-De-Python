# Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu 
# Índice de Massa Corporal (IMC) e mostre seu status, de acordo com a tabela abaixo:
# - IMC abaixo de 18,5: Abaixo do Peso
# - Entre 18,5 e 25: Peso Ideal
# - 25 até 30: Sobrepeso
# - 30 até 40: Obesidade
# - Acima de 40: Obesidade Mórbida

peso = float(input('Peso: '))
altura = float(input('Altura: '))
imc = peso/(altura ** 2)
print('Seu Índice de Massa Corporal (IMC) é de {:.2f}'.format(imc))
if imc < 18.5:
    print('Está ABAIXO do peso')
elif imc < 25:
    print('Está no peso IDEAL')
elif imc < 30:
    print('Está com SOBREPESO')
elif imc <  40:
    print('Está com OBESIDADE')
else:
    print('Está com OBESIDADE MÓBIDA')
print('Seu peso IDEAL é de {}')

#ideal = altura-100-((altura-150)/4)
#print(ideal)
    