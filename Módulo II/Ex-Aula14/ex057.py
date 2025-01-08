# Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores 
# 'M' ou 'F'. Caso esteja errado, peça a digitação novamente até ter um valor correto.
sexo = str(input('Informe seu sexo: [M/F] ')).strip().upper()[0]
while sexo not in  'MF': # Enquanto o sexo não estiver 'MmFf'
    sexo = str(input('Dados inválidos. Por favor, informe seu sexo: ')).strip().upper()[0]
if sexo == 'M':
    sexo = 'Masculino'
else:
    sexo = 'Feminino'
print('Sexo {} registrado com sucesso'.format(sexo))

# Foi adicionado as linhas de código if e else da resolução original 