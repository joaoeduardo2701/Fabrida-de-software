altura = float(input('Qual a altura da pessoa em metros: '))
sexo = input('Qual o sexo da pessoa [M/F]? ')

while sexo.upper() not in 'MF':
    print('Sexo inválido! Tente novamente.')
    sexo = str(input('Qual o sexo da pessoa [M/F]? '))

if sexo.upper() == 'M':
    peso_ideal = (72.7 * altura) - 58
else:
    peso_ideal = (62.1 * altura) - 44.7

print(f'O peso ideal da pessoa é de {peso_ideal:.2f}kg')
